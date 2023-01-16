from strenum import StrEnum

RUSTY_CAULDRON_KEY = 'RUSTY_CAULDRON_KEY'
SESSION_TOKEN = 'SESSION_TOKEN'

class ROUTES(StrEnum):
    Home = "/"
    Signup = "/signup"
    Login = "/login"
    Logout = "/logout"
    Recipes= "/recipes"
    AddRecipe = "/recipes/new"
    EditRecipe = "/recipes/<id>"
    MyRecipes = "/my-recipes"
