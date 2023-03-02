from tables.ingredients import Ingredient
from tables.recipes import Recipe
from utils.main import xstr

class RecipeService():
  def get_recipes(titleOpt, ingredients, page, per_page):
    # Get the necessary recipe ids from the asked ingredient list
    filteredIngredients = getRecipeIdsFromFilteredIngredients(ingredients)

    # If we don't find any ingredients we can return an empty list
    if filteredIngredients and len(filteredIngredients) == 0:
        return list()

    # Clean optional title
    title = xstr(titleOpt)
    # Prepare recipe title filter
    recipeFilter = Recipe.title.like(f"%{title}%")
    # Start recipe query
    query = Recipe.query.filter(recipeFilter)
    
    # If we have ingredient, add additional filter to the initial query
    if filteredIngredients:
        filteredIngredients = list(map(lambda i: i[0], filteredIngredients))
        query = query.filter(Recipe._id.in_(filteredIngredients))
    
    # Prepare order by
    order_by = Recipe.created_at.desc()
    # Add order by to query
    orderedQuery = query.order_by(order_by)
    # Run final query with pagination
    paginatedQuery = orderedQuery.paginate(page=page, per_page=per_page, error_out=False)
    return paginatedQuery

# Get optional recipe ids from ingredients
def getRecipeIdsFromFilteredIngredients(ingredients):
    if len(ingredients) == 0:
        return None
    filteredIngredientFilter = [Ingredient.name.like(f"%{ingredient}%") for ingredient in ingredients]
    return Ingredient.query.with_entities(Ingredient.recipe_id).filter(*filteredIngredientFilter).distinct().all()
