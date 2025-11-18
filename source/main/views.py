from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, View
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.db.models import Q

from constants import COOKING_MEASUREMENT
from recipe_service import RecipeService
from user_service import UserService
from utils.main import makeIngredientData, validate_password, validateIngredients
from tables.recipes import Recipe
from tables.ingredients import Ingredient


class GuestOnlyView(View):
    def dispatch(self, request, *args, **kwargs):
        # Redirect to the index page if the user already authenticated
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)


class IndexPageView(TemplateView):
    template_name = 'index.html'


@method_decorator(require_http_methods(["GET", "POST"]), name='dispatch')
class LoginPageView(GuestOnlyView):
    template_name = 'login.html'

    def get(self, request):
        form_data = {'email': '', 'password': ''}
        return render(request, self.template_name, {'form_data': form_data})

    def post(self, request):
        form_data = {
            'email': request.POST.get('email', ''),
            'password': request.POST.get('password', ''),
        }

        # Check email
        if not form_data['email']:
            messages.error(request, 'Email required')
            form_data['password'] = ''
            return render(request, self.template_name, {'form_data': form_data}), 400

        # Check password
        if not form_data['password']:
            messages.error(request, 'Password required')
            form_data['password'] = ''
            return render(request, self.template_name, {'form_data': form_data}), 400

        # Authenticate user
        user = authenticate(request, username=form_data['email'], password=form_data['password'])

        # If the user doesn't exist or the password isn't a match prompt the user
        if not user:
            messages.error(request, 'Invalid email or password')
            form_data['password'] = ''
            return render(request, self.template_name, {'form_data': form_data}), 400

        # Login the user
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')

        # Redirect the user
        return redirect(settings.LOGIN_REDIRECT_URL)


@method_decorator(require_http_methods(["GET", "POST"]), name='dispatch')
class SignupPageView(GuestOnlyView):
    template_name = 'signup.html'

    def get(self, request):
        form_data = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
            'confirmation': '',
        }
        return render(request, self.template_name, {'form_data': form_data})

    def post(self, request):
        form_data = {
            'first_name': request.POST.get('first_name', ''),
            'last_name': request.POST.get('last_name', ''),
            'email': request.POST.get('email', ''),
            'password': request.POST.get('password', ''),
            'confirmation': request.POST.get('confirmation', ''),
        }

        # Check first name
        if not form_data['first_name']:
            messages.error(request, 'First name is required')
            form_data['password'] = ''
            form_data['confirmation'] = ''
            return render(request, self.template_name, {'form_data': form_data}), 400

        # Check last name
        if not form_data['last_name']:
            messages.error(request, 'Last name is required')
            form_data['password'] = ''
            form_data['confirmation'] = ''
            return render(request, self.template_name, {'form_data': form_data}), 400

        # Check email
        if not form_data['email']:
            messages.error(request, 'Email is required')
            form_data['password'] = ''
            form_data['confirmation'] = ''
            return render(request, self.template_name, {'form_data': form_data}), 400

        # Check password
        if not form_data['password']:
            messages.error(request, 'Password is required')
            form_data['password'] = ''
            form_data['confirmation'] = ''
            return render(request, self.template_name, {'form_data': form_data}), 400

        # Check password confirmation
        if not form_data['confirmation']:
            messages.error(request, 'Please confirm your password')
            form_data['password'] = ''
            form_data['confirmation'] = ''
            return render(request, self.template_name, {'form_data': form_data}), 400

        # Validate the password
        password_error_msg = validate_password(
            form_data['password'],
            form_data['confirmation'],
        )
        if password_error_msg:
            messages.error(request, password_error_msg)
            form_data['password'] = ''
            form_data['confirmation'] = ''
            return render(request, self.template_name, {'form_data': form_data}), 400

        # Check if email is in use
        user = UserService.get_user_by_email(form_data['email'])
        if user:
            messages.error(request, 'Email is already in use')
            form_data['password'] = ''
            form_data['confirmation'] = ''
            return render(request, self.template_name, {'form_data': form_data}), 400

        # Create user
        UserService.create_user(
            first_name=form_data['first_name'],
            last_name=form_data['last_name'],
            email=form_data['email'],
            password=form_data['password']
        )
        messages.success(request, 'Account created successfully. Please login.')
        return redirect('/login/')


@method_decorator(require_http_methods(["GET"]), name='dispatch')
class RecipesPageView(TemplateView):
    template_name = 'recipes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get('title', '')
        ingredients = self.request.GET.get('ingredients', '')
        page = int(self.request.GET.get('page', '1'))
        per_page = int(self.request.GET.get('per_page', '10'))
        ingredient_list = list(
            filter(None, map(lambda i: i.strip(), ingredients.split(',')))
        )

        paginated_recipes, ingredients_map = RecipeService.get_recipes(
            user_id=None,
            title_opt=title,
            ingredients=ingredient_list,
            page=page,
            per_page=per_page,
        )

        # Create pagination object compatible with template
        # Make it iterable like Flask pagination
        class PaginationWrapper:
            def __init__(self, page_obj, per_page):
                self.page_obj = page_obj
                self.items = list(page_obj)
                self.page = page_obj.number
                self.pages = page_obj.paginator.num_pages
                self.per_page = per_page
                self.total = page_obj.paginator.count
                self.has_prev = page_obj.has_previous()
                self.has_next = page_obj.has_next()
                self.prev_num = page_obj.previous_page_number() if page_obj.has_previous() else None
                self.next_num = page_obj.next_page_number() if page_obj.has_next() else None
                self.first = (page_obj.number - 1) * per_page + 1 if page_obj.number > 0 else 0
                self.last = min(page_obj.number * per_page, page_obj.paginator.count)
            
            def iter_pages(self):
                return self.page_obj.paginator.page_range
            
            def __iter__(self):
                return iter(self.items)
        
        pagination_obj = PaginationWrapper(paginated_recipes, per_page)

        context.update({
            'recipes': pagination_obj,
            'ingredientsMap': ingredients_map,
            'title': title,
            'ingredients': ingredients,
            'page': page,
            'per_page': per_page,
        })
        return context


@method_decorator(require_http_methods(["GET", "POST"]), name='dispatch')
class AddRecipe(LoginRequiredMixin, View):
    template_name = 'add-recipe.html'

    def get(self, request):
        default_ingredient_list = [{
            'name': '',
            'amount': '1',
            'measurement': COOKING_MEASUREMENT.cl,
        }]
        return render(request, self.template_name, {
            'ingredient_list': default_ingredient_list,
        })

    def post(self, request):
        ingredient_name_list = request.POST.getlist('ingredient')
        amount_list = request.POST.getlist('amount')
        measurement_list = request.POST.getlist('measurement')

        ingredient_list = list(map(
            makeIngredientData,
            zip(ingredient_name_list, amount_list, measurement_list)
        ))
        title = request.POST.get('title', '')
        prep_time = request.POST.get('prep_time')
        cooking_time = request.POST.get('cooking_time')
        description = request.POST.get('description', '')

        # Check title
        if not title:
            messages.error(request, 'Title is required')
            return render(request, self.template_name, {
                'title': title,
                'prep_time': prep_time,
                'cooking_time': cooking_time,
                'ingredient_list': ingredient_list,
                'description': description,
            }), 400

        # Check preparation time
        if prep_time and not prep_time.isdigit():
            messages.error(request, 'Preparation time must be a number')
            return render(request, self.template_name, {
                'title': title,
                'prep_time': prep_time,
                'cooking_time': cooking_time,
                'ingredient_list': ingredient_list,
                'description': description,
            }), 400

        # Check cooking time
        if not cooking_time:
            messages.error(request, 'Cooking time is required')
            return render(request, self.template_name, {
                'title': title,
                'prep_time': prep_time,
                'cooking_time': cooking_time,
                'ingredient_list': ingredient_list,
                'description': description,
            }), 400

        if not cooking_time.isdigit():
            messages.error(request, 'Cooking time must be a number')
            return render(request, self.template_name, {
                'title': title,
                'prep_time': prep_time,
                'cooking_time': cooking_time,
                'ingredient_list': ingredient_list,
                'description': description,
            }), 400

        # Check ingredients
        ingredients_error_msg = validateIngredients(ingredient_list)
        if ingredients_error_msg:
            messages.error(request, ingredients_error_msg)
            return render(request, self.template_name, {
                'title': title,
                'prep_time': prep_time,
                'cooking_time': cooking_time,
                'ingredient_list': ingredient_list,
                'description': description,
            }), 400

        # Check description
        if not description:
            messages.error(request, 'Description is required')
            return render(request, self.template_name, {
                'title': title,
                'prep_time': prep_time,
                'cooking_time': cooking_time,
                'ingredient_list': ingredient_list,
                'description': description,
            }), 400

        user_id = request.user.id
        RecipeService.insert_recipe(
            user_id,
            title=title,
            prep_time=prep_time,
            cooking_time=cooking_time,
            ingredient_list=ingredient_list,
            description=description,
        )

        messages.success(request, 'Recipe added')
        return redirect('/add-recipe/')


@method_decorator(require_http_methods(["GET"]), name='dispatch')
class RecipePageView(TemplateView):
    template_name = 'recipe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_id = kwargs.get('recipe_id')
        recipe, ingredient_list = RecipeService.find_recipe_by_id(recipe_id)
        
        if not recipe:
            return redirect('/not-found-page/')
        
        context.update({
            'recipe': recipe,
            'ingredient_list': ingredient_list,
        })
        return context


@method_decorator(require_http_methods(["GET"]), name='dispatch')
class MyRecipesPageView(LoginRequiredMixin, TemplateView):
    template_name = 'my-recipes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get('title', '')
        ingredients = self.request.GET.get('ingredients', '')
        page = int(self.request.GET.get('page', '1'))
        per_page = int(self.request.GET.get('per_page', '10'))
        ingredient_list = list(
            filter(None, map(lambda i: i.strip(), ingredients.split(',')))
        )

        paginated_recipes, ingredients_map = RecipeService.get_recipes(
            user_id=self.request.user.id,
            title_opt=title,
            ingredients=ingredient_list,
            page=page,
            per_page=per_page,
        )

        # Create pagination object compatible with template
        # Make it iterable like Flask pagination
        class PaginationWrapper:
            def __init__(self, page_obj, per_page):
                self.page_obj = page_obj
                self.items = list(page_obj)
                self.page = page_obj.number
                self.pages = page_obj.paginator.num_pages
                self.per_page = per_page
                self.total = page_obj.paginator.count
                self.has_prev = page_obj.has_previous()
                self.has_next = page_obj.has_next()
                self.prev_num = page_obj.previous_page_number() if page_obj.has_previous() else None
                self.next_num = page_obj.next_page_number() if page_obj.has_next() else None
                self.first = (page_obj.number - 1) * per_page + 1 if page_obj.number > 0 else 0
                self.last = min(page_obj.number * per_page, page_obj.paginator.count)
            
            def iter_pages(self):
                return self.page_obj.paginator.page_range
            
            def __iter__(self):
                return iter(self.items)
        
        pagination_obj = PaginationWrapper(paginated_recipes, per_page)

        context.update({
            'recipes': pagination_obj,
            'ingredientsMap': ingredients_map,
            'title': title,
            'ingredients': ingredients,
            'page': page,
            'per_page': per_page,
        })
        return context


@method_decorator(require_http_methods(["POST"]), name='dispatch')
class DeleteRecipe(LoginRequiredMixin, View):
    def post(self, request, recipe_id):
        user_id = request.user.id

        if str(user_id) != request.POST.get('owner_user_id'):
            messages.error(request, 'You are not allowed to perform this action')
            return redirect(f'/recipe/{recipe_id}/')

        RecipeService.mark_recipe_as_deleted(user_id, recipe_id)
        messages.success(request, 'Recipe deleted')
        return redirect('/recipes/')


@method_decorator(require_http_methods(["POST"]), name='dispatch')
class UpdateRecipe(LoginRequiredMixin, View):
    def post(self, request, recipe_id):
        user_id = request.user.id

        if str(user_id) != request.POST.get('owner_user_id'):
            messages.error(request, 'You are not allowed to perform this action')
            return redirect(f'/recipe/{recipe_id}/')

        ingredient_name_list = request.POST.getlist('ingredient')
        amount_list = request.POST.getlist('amount')
        measurement_list = request.POST.getlist('measurement')

        ingredient_list = list(map(
            makeIngredientData,
            zip(ingredient_name_list, amount_list, measurement_list)
        ))
        title = request.POST.get('title', '')
        prep_time = request.POST.get('prep_time')
        cooking_time = request.POST.get('cooking_time')
        description = request.POST.get('description', '')

        # Check title
        if not title:
            messages.error(request, 'Title is required')
            return redirect(f'/recipe/{recipe_id}/')

        # Check preparation time
        if prep_time and not prep_time.isdigit():
            messages.error(request, 'Preparation time must be a number')
            return redirect(f'/recipe/{recipe_id}/')

        # Check cooking time
        if not cooking_time:
            messages.error(request, 'Cooking time is required')
            return redirect(f'/recipe/{recipe_id}/')

        if not cooking_time.isdigit():
            messages.error(request, 'Cooking time must be a number')
            return redirect(f'/recipe/{recipe_id}/')

        # Check ingredients
        ingredients_error_msg = validateIngredients(ingredient_list)
        if ingredients_error_msg:
            messages.error(request, ingredients_error_msg)
            return redirect(f'/recipe/{recipe_id}/')

        # Check description
        if not description:
            messages.error(request, 'Description is required')
            return redirect(f'/recipe/{recipe_id}/')

        RecipeService.update_recipe(
            recipe_id=recipe_id,
            title=title,
            prep_time=prep_time,
            cooking_time=cooking_time,
            ingredient_list=ingredient_list,
            description=description,
        )

        messages.success(request, 'Recipe updated')
        return redirect(f'/recipe/{recipe_id}')


class NotFoundPageView(TemplateView):
    template_name = 'not-found-page.html'
