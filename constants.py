from strenum import StrEnum

RUSTY_CAULDRON_KEY = 'RUSTY_CAULDRON_KEY'
MIN_PASSWORD_LENGTH = 8

class ExtendedEnum(StrEnum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

class ROUTES(ExtendedEnum):
    Home = "/"
    Signup = "/signup"
    Login = "/login"
    Logout = "/logout"
    Recipes= "/recipes"
    AddRecipe = "/recipes/new"
    Recipe = "/recipes/<id>"
    MyRecipes = "/my-recipes"

class COOKING_MEASUREMENT(ExtendedEnum):
    cl = "centilitre"
    cup = "cup"
    dkg = "dekagram"
    dl = "decilitre"
    fl = "fluid-ounce"
    g = "gramm"
    gal = "gallon"
    kg = "kilogram"
    l = "litre"
    lb = "pound"
    mg = "miligram"
    ml = "millilitre"
    oz = "ounce"
    pt = "pint"
    qt = "quart"
    t = "tonne"
    tbs = "tablespoon"
    tsp = "teaspoon"
