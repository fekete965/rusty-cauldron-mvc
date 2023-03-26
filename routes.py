from flask import flash, redirect, render_template, request
from flask_login import current_user, login_required, login_user, logout_user
from login_manager import unauthenticated_route
from recipe_service import RecipeService
from dateutil import parser
from user_service import UserService

from utils.main import validate_password, validateIngredients
from constants import COOKING_MEASUREMENT, ROUTES
from app import App
from werkzeug.security import generate_password_hash, check_password_hash


@App.template_filter('format_string_date')
def format_string_date(date, fmt=None):
    date = parser.parse(date)
    native = date.replace(tzinfo=None)
    if not fmt:
        fmt='%Y-%m-%d'
    return native.strftime(fmt)

# Define Home route
@App.route(ROUTES.Home, methods=["GET"])
def index():
	return render_template("index.html")


# Define Signup route
@App.route(ROUTES.Signup, methods=["GET", "POST"])
@unauthenticated_route
def sign_up():
	if (request.method == "GET"):
		return render_template("signup.html", form_data=None)

	form_data = {
		"first_name": request.form.get("firstName"),
		"last_name": request.form.get("lastName"),
		"email": request.form.get("email"),
		"password": request.form.get("password"),
		"confirmation": request.form.get("confirmation"),
	}
	
 	# Check first name
	if not form_data["first_name"]:
		flash("First name is required")
		return render_template("signup.html", form_data=form_data), 400

	# Check last name
	if not form_data["last_name"]:
		flash("Last name is required")
		return render_template("signup.html", form_data=form_data), 400

	# Check email
	if not form_data["email"]:
		flash("Email is required")
		return render_template("signup.html", form_data=form_data), 400

	# Check password
	if not form_data["password"]:
		flash("Password is required")
		return render_template("signup.html", form_data=form_data), 400

	# Check password confirmation
	if not form_data["confirmation"]:
		flash("Please confirm your password")
		return render_template("signup.html", form_data=form_data), 400

	# Validate the password
	password_error_msg = validate_password(form_data["password"], form_data["confirmation"])
	if password_error_msg:
		flash(password_error_msg)
		form_data.pop("password")
		form_data.pop("confirmation")
		return render_template("signup.html", form_data=form_data), 400

	# Check if email is in use
	user = UserService.get_user_by_email(form_data["email"])
	if user:
		flash("Email is already in use")
		return render_template("signup.html"), 400	

	# Call userService to create a user
	UserService.create_user(form_data['first_name'], form_data['last_name'], form_data['email'], generate_password_hash(form_data['password']))
	return redirect(ROUTES.Login)


# Define Login route
@App.route(ROUTES.Login, methods=["GET", "POST"])
@unauthenticated_route
def login():
	if (request.method == "GET"):
		return render_template("login.html", form_data=None)

	# Get form values
	form_data = {
		"email": request.form.get("email"),
		"password": request.form.get("password"),
	}
 
	# Check email
	if not form_data["email"]:
		flash("Email required")
		return render_template("login.html", form_data=form_data), 400
	# Check password
	if not form_data["password"]:
		flash("Password required")
		return render_template("login.html", form_data=form_data), 400
 
	# Call userService to find the user
	user = UserService.get_user_by_email(form_data["email"])
	
	# If the user doesn't exist or the password isn't a match prompt the user
	if not user or not check_password_hash(user.password, form_data["password"]):
		flash("Invalid email or password")
		form_data.pop("password")
		return render_template("login.html", form_data=form_data), 400

	# Get the user and save it
	login_user(user, remember=True)

	# Redirect the user
	return redirect(next or ROUTES.Home)


# Define Logout route
@App.route(ROUTES.Logout, methods=["GET", "POST"])
def logout():
	# Logout the user
	logout_user()
	return redirect(ROUTES.Home)


# Define Recipes route
@App.route(ROUTES.Recipes, methods=["GET"])
def recipes():
	args = request.args
	title = args.get("title", "")
	ingredients = args.get("ingredients", "")
	page = int(args.get("page", "1"))
	per_page = int(args.get("per_page", "10"))
	ingredient_list = list(filter(None, map(lambda i: i.strip(), ingredients.split(","))))

	(recipes, ingredientsMap) = RecipeService.get_recipes(user_id=None, title_opt=title, ingredients=ingredient_list, page=page, per_page=per_page)
 
	return render_template("recipes.html", recipes=recipes, ingredientsMap=ingredientsMap, title=title, ingredients=ingredients, page=page, per_page=per_page)


# Define Add Recipe route
@App.route(ROUTES.AddRecipe, methods=["GET", "POST"])
@login_required
def add_recipe():

	defaultFormData = {
		"ingredient_dataset": [{ "value": "", "measurement": COOKING_MEASUREMENT.cl }],
	}

	if (request.method == "GET"):
		return render_template("add-recipe.html", form_data=defaultFormData)

	def makeIngredientData(dataTuple):
		return { "value": dataTuple[0], "measurement": dataTuple[1] }

	ingredient_list = request.form.getlist("ingredient")
	measurement_list = request.form.getlist("measurement")
	ingredient_dataset = list(map(makeIngredientData, zip(ingredient_list, measurement_list)))

	form_data = {
		"title": request.form.get("title", ""),
		"prep_time": request.form.get("prep_time"),
		"cooking_time": request.form.get("cooking_time"),
  		"ingredient_dataset" : ingredient_dataset,
		"description": request.form.get("description"),
	}
 
	# Check title
	if not form_data["title"]:
		flash("Title is required")
		return render_template("add-recipe.html", form_data=form_data), 400
	# Check preparation time
	if (form_data["prep_time"] and not form_data["prep_time"].isdigit()):
		flash("Preparation time must be a number")
		return render_template("add-recipe.html", form_data=form_data), 400
	# Check cooking time
	if not form_data["cooking_time"]:
		flash("Cooking time is required")
		return render_template("add-recipe.html", form_data=form_data), 400
	if not form_data["cooking_time"].isdigit():
		flash("Cooking time must be a number")
		return render_template("add-recipe.html", form_data=form_data), 400
	# Check description
	if not form_data["description"]:
		flash("Description is required")
		return render_template("add-recipe.html", form_data=form_data), 400
	# Check ingredients
	# ingredients_error_msg = validateIngredients(form_data["ingredient_list"])
	# if ingredients_error_msg:
	# 	flash(ingredients_error_msg)
	# 	return render_template("add-recipe.html", form_data=form_data), 400
 
 	# Check ingredients
	# measurements_error_msg = validateMeasurement(form_data["measurement_list"])
	# if measurements_error_msg:
	# 	flash(measurements_error_msg)
	# 	return render_template("add-recipe.html", form_data=form_data), 400

	# Validate the form, save the record into the DB and redirect the user
	return redirect(ROUTES.AddRecipe)


# Define Recipe route
@App.route(ROUTES.Recipe, methods=["DELETE", "GET", "PUT"])
def recipe(id):
	# Return the recipe information to the user
	if (request.method == "GET"):
		# Get the recipe from the DB based on its id and return it to the user
		# recipe = recipe_service.get_recipe(id)
		recipe = None # <-- Dummy value for now
		return render_template("update-recipe.html", recipe=recipe)
	
	# Mark recipe as deleted
	if (request.method == "DELETE"):
		# Find the recipe, and mark as deleted in the database
		return render_template("update-recipe.html")
	
  	# Check title
	title = request.form.get("title")
	if not title:
		flash("Title is required")
		return render_template("update-recipe.html"), 400

	# Check preparation time
	prep_time = request.form.get("prepTime")
	if (prep_time and not prep_time.isdigit()):
		flash("Preparation time must be a number")
		return render_template("update-recipe.html"), 400

	# Check cooking time
	cooking_time = request.form.get("cookingTime")
	if not cooking_time:
		flash("Cooking time is required")
		return render_template("update-recipe.html"), 400
	if not cooking_time.isdigit():
		flash("Cooking time must be a number")
		return render_template("update-recipe.html"), 400

	# Check description
	description = request.form.get("description")
	if not description:
		flash("Description is required")
		return render_template("update-recipe.html"), 400

	# Check ingredients
	ingredients = request.form.getlist("ingredients")
	ingredients_error_msg = validateIngredients(ingredients)
	if ingredients_error_msg:
		flash(ingredients_error_msg)
		return render_template("update-recipe.html"), 400
	
	# Validate the form, save the record into the DB and redirect the user
	return redirect(ROUTES.Recipe.replace("<id>", id))


# Define My Recipes route
@App.route(ROUTES.MyRecipes, methods = ["GET", "POST"])
@login_required
def user_recipes():

	if request.method == "GET":
		# Get the user's active recipes from the DB based
		args = request.args
		title = args.get("title", "")
		ingredients = args.get("ingredients", "")
		page = int(args.get("page", "1"))
		per_page = int(args.get("per_page", "10"))
		ingredient_list = list(filter(None, map(lambda i: i.strip(), ingredients.split(","))))

		(recipes, ingredientsMap) = RecipeService.get_recipes(user_id=current_user.get_id(), title_opt=title, ingredients=ingredient_list, page=page, per_page=per_page)
 
		return render_template("my-recipes.html", recipes=recipes, ingredientsMap=ingredientsMap, title=title, ingredients=ingredients, page=page, per_page=per_page)

# Define 404 page
@App.errorhandler(404)
def not_found_page(error):
	return render_template('not-found-page.html'), 404
