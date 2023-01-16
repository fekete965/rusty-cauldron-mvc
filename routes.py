from flask import abort, make_response, redirect, render_template, request, session
from flask_login import login_required, login_user, logout_user
from constants import ROUTES, SESSION_TOKEN
from utils import isUrlSafe
from app import App

@App.route(ROUTES.Home)
def index():
    return render_template("index.html")


@App.route(ROUTES.Signup, methods=["GET", "POST"])
def signUp():
	if (request.method == "GET"):
		return render_template("signup.html")

	# Do form validation, and save user to the DB and redirect user to login page
	return redirect(ROUTES.Login)


@App.route(ROUTES.Login, methods=["GET", "POST"])
def login():
    if (request.method == "GET"):
        return render_template("login.html")

    next = request.args.get("next")
    if not isUrlSafe(next):
        return abort(400)

    # Get the user and save it
    login_user("", remember=True)

    resp = make_response(redirect(next or ROUTES.Home))
    return resp


@App.route(ROUTES.Logout, methods=["POST"])
@login_required
def logout():
  # logout the user by removing the session from the cookies and mark it expired in the DB
	logout_user()
	return redirect("/")


@App.route(ROUTES.Recipes, methods=["GET", "POST"])
def recipes():
    if (request.method == "GET"):
        return render_template("recipes.html")
    
    # Validate form, filter recipes and return the new data to the user
    return render_template("recipes.html")


@App.route(ROUTES.AddRecipe, methods=["GET", "POST"])
@login_required
def addRecipe():
    if (request.method == "GET"):
        return render_template("add-recipe.html")
    
    # Validate the form, save the record into the DB and redirect the user
    return redirect(ROUTES.AddRecipe)


@App.route(ROUTES.EditRecipe, methods=["GET", "PUT"])
@login_required
def editRecipe(id):
    if (request.method == "GET"):
        # Get the recipe from the DB based on its id and return it to the user
        return render_template("update-recipe.html")
    
    # Validate the form, save the record into the DB and redirect the user
    return redirect(ROUTES.EditRecipe.replace("<id>", id))


@App.route(ROUTES.MyRecipes)
@login_required
def userRecipes():
	# Get the user's recipes from the DB
	return render_template("my-recipes.html")


@App.errorhandler(404)
def notFoundPage(error):
    return render_template('not-found-page.html'), 404
