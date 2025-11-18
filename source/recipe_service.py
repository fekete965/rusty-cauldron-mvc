from django.core.paginator import Paginator
from django.db.models import Q

from tables.ingredients import Ingredient
from tables.recipes import Recipe
from utils.main import xstr


class RecipeService:
    @staticmethod
    def to_ingredient(recipe_id):
        def fn(ingredient):
            return Ingredient(
                recipe_id=recipe_id,
                name=ingredient["name"],
                amount=ingredient["amount"],
                measurement=ingredient["measurement"],
            )

        return fn

    @staticmethod
    def get_recipe_ids_from_filtered_ingredients(ingredients):
        """Get recipe IDs that match the ingredient filters"""
        if len(ingredients) == 0:
            return None

        # Build Q objects for ingredient name filtering
        ingredient_filters = Q()
        for ingredient in ingredients:
            ingredient_filters |= Q(name__icontains=ingredient, deleted=False)

        recipe_ids = (
            Ingredient.objects.filter(ingredient_filters)
            .values_list("recipe_id", flat=True)
            .distinct()
        )

        return list(recipe_ids)

    @staticmethod
    def get_recipes(user_id, title_opt, ingredients, page, per_page):
        """Get recipes with pagination and ingredient filtering"""
        # Get the necessary recipe ids from the asked ingredient list
        filtered_ingredients = RecipeService.get_recipe_ids_from_filtered_ingredients(ingredients)

        # If we don't find any ingredients we can return an empty list
        if filtered_ingredients is not None and len(filtered_ingredients) == 0:
            return (Paginator([], per_page).page(1), {})

        # Clean optional title
        title = xstr(title_opt)

        # Start recipe query
        query = Recipe.objects.filter(deleted=False)

        # Filter by title if provided
        if title:
            query = query.filter(title__icontains=title)

        # Filter by user_id if needed
        if user_id:
            query = query.filter(user_id=user_id)

        # If we have ingredient filters, add additional filter to the initial query
        if filtered_ingredients:
            query = query.filter(id__in=filtered_ingredients)

        # Order by created_at descending
        query = query.order_by("-created_at")

        # Paginate
        paginator = Paginator(query, per_page)
        paginated_recipes = paginator.page(page)

        # Get ingredients for recipes on this page
        recipe_ids_on_page = [r.id for r in paginated_recipes]
        ingredients_per_recipe = {}
        for recipe_id in recipe_ids_on_page:
            ingredients = (
                Ingredient.objects.filter(recipe_id=recipe_id, deleted=False).order_by("name").all()
            )
            ingredients_per_recipe[recipe_id] = list(ingredients)

        return (paginated_recipes, ingredients_per_recipe)

    @staticmethod
    def insert_recipe(user_id, title, prep_time, cooking_time, ingredient_list, description):
        """Create a new recipe with ingredients"""
        new_recipe = Recipe(
            user_id=user_id,
            title=title,
            prep_time=int(prep_time) if prep_time else None,
            cooking_time=int(cooking_time) if cooking_time else None,
            description=description,
        )
        new_recipe.save()

        # Create ingredients
        new_ingredients = []
        for ingredient_data in ingredient_list:
            ingredient = Ingredient(
                recipe=new_recipe,
                name=ingredient_data["name"],
                amount=float(ingredient_data["amount"]),
                measurement=ingredient_data["measurement"],
            )
            new_ingredients.append(ingredient)

        Ingredient.objects.bulk_create(new_ingredients)
        return True

    @staticmethod
    def mark_recipe_as_deleted(user_id, recipe_id):
        """Mark a recipe as deleted"""
        Recipe.objects.filter(user_id=user_id, id=recipe_id).update(deleted=True)
        return True

    @staticmethod
    def find_recipe_by_id(recipe_id):
        """Find a recipe by ID with its ingredients"""
        try:
            recipe = Recipe.objects.get(id=recipe_id, deleted=False)
            ingredients = (
                Ingredient.objects.filter(recipe_id=recipe_id, deleted=False).order_by("name").all()
            )
            return (recipe, list(ingredients))
        except Recipe.DoesNotExist:
            return (None, [])

    @staticmethod
    def update_recipe(recipe_id, title, prep_time, cooking_time, ingredient_list, description):
        """Update an existing recipe and its ingredients"""
        # Update existing recipe
        Recipe.objects.filter(id=recipe_id).update(
            title=title,
            prep_time=int(prep_time) if prep_time else None,
            cooking_time=int(cooking_time) if cooking_time else None,
            description=description,
        )

        # Mark existing ingredients as deleted
        Ingredient.objects.filter(recipe_id=recipe_id, deleted=False).update(deleted=True)

        # Create new ingredients
        recipe = Recipe.objects.get(id=recipe_id)
        new_ingredients = []
        for ingredient_data in ingredient_list:
            ingredient = Ingredient(
                recipe=recipe,
                name=ingredient_data["name"],
                amount=float(ingredient_data["amount"]),
                measurement=ingredient_data["measurement"],
            )
            new_ingredients.append(ingredient)

        Ingredient.objects.bulk_create(new_ingredients)
        return True
