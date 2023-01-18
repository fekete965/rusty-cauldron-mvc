from strenum import StrEnum

RUSTY_CAULDRON_KEY = 'RUSTY_CAULDRON_KEY'
MIN_PASSWORD_LENGTH = 8

class ROUTES(StrEnum):
    Home = "/"
    Signup = "/signup"
    Login = "/login"
    Logout = "/logout"
    Recipes= "/recipes"
    AddRecipe = "/recipes/new"
    EditRecipe = "/recipes/<id>"
    MyRecipes = "/my-recipes"
