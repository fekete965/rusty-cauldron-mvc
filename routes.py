from curses import flash
from flask import abort, make_response, redirect, render_template, request, session
from flask_login import login_required, login_user, logout_user

from utils.main import isUrlSafe, validatePassword
from constants import ROUTES
from app import App

# Define Home route
@App.route(ROUTES.Home)
def index():
    return render_template("index.html")


# Define Signup route
@App.route(ROUTES.Signup, methods=["GET", "POST"])
def signUp():
	if (request.method == "GET"):
		return render_template("signup.html")

	# Gather form values
	firstName = request.form.get("firstName")
	lastName = request.form.get("lastName")
	email = request.form.get("email")
	password = request.form.get("password")
	confirmation = request.form.get("confirmation")

	# Check first name
	if not firstName:
		flash("First name is required")
		return render_template("signup.html"), 400
	# Check last name
	if not lastName:
		flash("Last name is required")
		return render_template("signup.html"), 400
	# Check email
	if not email:
		flash("Email is required")
		return render_template("signup.html"), 400
	# Check password
	if not password:
		flash("Password is required")
		return render_template("signup.html"), 400
	# Check password confirmation
	if not confirmation:
		flash("Please confirm your password")
		return render_template("signup.html"), 400

	# Validate the password
	passwordErrorMsg = validatePassword(password, confirmation)
	if passwordErrorMsg:
		flash(passwordErrorMsg)
		return render_template("signup.html"), 400

	# Check if email is in use
	# user = db.execute("SELECT * FROM users WHERE username = ? LIMIT 1;", username)

	if len(user) != 0:
		flash("Email is already in use")
		return render_template("signup.html"), 400	

	# Call userService to create a user
 	# userService.createUser(firstName, lastName, email, password)
	return redirect(ROUTES.Login)


# Define Login route
@App.route(ROUTES.Login, methods=["GET", "POST"])
def login():
	if (request.method == "GET"):
		return render_template("login.html")

	# Get form values
	email = request.form.get("email")
	password = request.form.get("password")
 
	# Check email
	if not email:
		flash("Email required")
		return render_template("login.html"), 400
	# Check password
	if not password:
		flash("Password required")
		return render_template("login.html"), 400
 
	# Call userService to login the user
 	# user = userService.loginUser(email, password)

	# Prompt the user 
	if not user:
		flash("Incorrect email or password")
		return render_template("login.html"), 400

	# Check if next url exists
	next = request.args.get("next")
	if not isUrlSafe(next):
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
@App.route(ROUTES.Recipes, methods=["GET", "POST"])
def recipes():
    if (request.method == "GET"):
        return render_template("recipes.html")
    
    # Validate form, filter recipes and return the new data to the user
    return render_template("recipes.html")


# Define Add Recipe route
@App.route(ROUTES.AddRecipe, methods=["GET", "POST"])
@login_required
def addRecipe():
    if (request.method == "GET"):
        return render_template("add-recipe.html")
    
    # Validate the form, save the record into the DB and redirect the user
    return redirect(ROUTES.AddRecipe)


# Define Edit Recipe route
@App.route(ROUTES.EditRecipe, methods=["GET", "PUT"])
@login_required
def editRecipe(id):
    if (request.method == "GET"):
        # Get the recipe from the DB based on its id and return it to the user
        return render_template("update-recipe.html")
    
    # Validate the form, save the record into the DB and redirect the user
    return redirect(ROUTES.EditRecipe.replace("<id>", id))


# Define My Recipes route
@App.route(ROUTES.MyRecipes)
@login_required
def userRecipes():
	# Get the user's recipes from the DB
	return render_template("my-recipes.html")


# Define 404 page
@App.errorhandler(404)
def notFoundPage(error):
    return render_template('not-found-page.html'), 404
