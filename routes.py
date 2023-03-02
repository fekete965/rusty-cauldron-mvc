from flask import abort, flash, make_response, redirect, render_template, request, session
from flask_login import login_required, login_user, logout_user
from recipeService import RecipeService

from utils.main import is_url_safe, validate_password, validateIngredients
from constants import ROUTES
from app import App
from werkzeug.security import generate_password_hash, check_password_hash

# Define Home route
@App.route(ROUTES.Home, methods=["GET"])
def index():
	return render_template("index.html")


# Define Signup route
@App.route(ROUTES.Signup, methods=["GET", "POST"])
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
	# user = db.execute("SELECT * FROM users WHERE email = ? LIMIT 1;", email)
	user = None # <-- Dummy value for now
	if len(user) != 0:
		flash("Email is already in use")
		return render_template("signup.html"), 400	

	# Call userService to create a user
 	# user_service.create_user(first_name, last_name, email, generate_password_hash(password))
	return redirect(ROUTES.Login)


# Define Login route
@App.route(ROUTES.Login, methods=["GET", "POST"])
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
 
	# Call userService to login the user
 	# user = user_service.login_user(form_data["email"], form_data["password"])
	user = None # <-- Dummy value for now
	# Prompt the user 
	if not user:
		flash("Incorrect email or password")
		form_data.pop("password")
		return render_template("login.html", form_data=form_data), 400

	# Check if next url exists
	next = request.args.get("next")
	if not is_url_safe(next):
		return abort(400)

	# Get the user and save it
	login_user("", remember=True)

	# Redirect the user
	resp = make_response(redirect(next or ROUTES.Home))
	return resp


# Define Logout route
@App.route(ROUTES.Logout, methods=["POST"])
@login_required
def logout():
  # logout the user by removing the session from the cookies and mark it expired in the DB
	logout_user()
	return redirect("/")


# Define Recipes route
@App.route(ROUTES.Recipes, methods=["GET"])
def recipes():
	args = request.args
	title = args.get("title")
	ingredients = args.get("ingredients", "")
	page = int(args.get("page", "1"))
	per_page = int(args.get("per_page", "10"))
	ingredient_list = list(filter(None, map(lambda i: i.strip(), ingredients.split(","))))

	recipes = RecipeService.get_recipes(title, ingredient_list, page, per_page)
 
	return render_template("recipes.html", recipes=recipes, title=title, ingredients=ingredients, page=page, per_page=per_page)


# Define Add Recipe route
@App.route(ROUTES.AddRecipe, methods=["GET", "POST"])
@login_required
def add_recipe():
	if (request.method == "GET"):
		return render_template("add-recipe.html")
	# Check title
	title = request.form.get("title")
	if not title:
		flash("Title is required")
		return render_template("add-recipe.html"), 400
	# Check preparation time
	prep_time = request.form.get("prepTime")
	if (prep_time and not prep_time.isdigit()):
		flash("Preparation time must be a number")
		return render_template("add-recipe.html"), 400
	# Check cooking time
	cooking_time = request.form.get("cookingTime")
	if not cooking_time:
		flash("Cooking time is required")
		return render_template("add-recipe.html"), 400
	if not cooking_time.isdigit():
		flash("Cooking time must be a number")
		return render_template("add-recipe.html"), 400
	# Check description
	description = request.form.get("description")
	if not description:
		flash("Description is required")
		return render_template("add-recipe.html"), 400
	# Check ingredients
	ingredients = request.form.getlist("ingredients")
	ingredients_error_msg = validateIngredients(ingredients)
	if ingredients_error_msg:
		flash(ingredients_error_msg)
		return render_template("add-recipe.html"), 400
 
	# Validate the form, save the record into the DB and redirect the user
	return redirect(ROUTES.AddRecipe)


# Define Recipe route
@App.route(ROUTES.Recipe, methods=["DELETE", "GET", "PUT"])
@login_required
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
	recipes = None

	if request.method == "GET":
		# Get the user's active recipes from the DB based
		# recipes = recipe_service.get_my_recipes(user_id)
		return render_template("my-recipes.html", recipes=recipes)

	include_deleted = request.form.get("includeDeleted", False)
	if include_deleted:
		# recipes = recipe_service.get_my_recipes(user_id, deleted=true)
		recipes = None # <-- Dummy value for now
	else:
		# recipes = recipe_service.get_my_recipes(user_id)
		recipes = None # <-- Dummy value for now
  
	return render_template("my-recipes.html", recipes=recipes)

# Define 404 page
@App.errorhandler(404)
def not_found_page(error):
	return render_template('not-found-page.html'), 404
