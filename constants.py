from strenum import StrEnum

RUSTY_CAULDRON_KEY = 'RUSTY_CAULDRON_KEY'
MIN_PASSWORD_LENGTH = 8

class ExtendedEnum(StrEnum):
    @classmethod
    def nameList(cls):
        return list(map(lambda c: c.name, cls))
    
    @classmethod
    def valueList(cls):
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
    large = "large"
    lb = "pound"
    medium = "medium"
    mg = "miligram"
    ml = "millilitre"
    oz = "ounce"
    package = "package"
    pt = "pint"
    qt = "quart"
    small = "small"
    t = "tonne"
    tbs = "tablespoon"
    tsp = "teaspoon"
