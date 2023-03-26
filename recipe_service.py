from tables.ingredients import Ingredient
from tables.recipes import Recipe
from utils.main import xstr
from app import db

class RecipeService():
	# Get optional recipe ids from ingredients
	def get_recipe_ids_from_filtered_ingredients(ingredients):
		if len(ingredients) == 0:
			return None
		filteredIngredientFilter = [Ingredient.name.like(f"%{ingredient}%") for ingredient in ingredients]
		return Ingredient.query.with_entities(Ingredient.recipe_id).filter(*filteredIngredientFilter).distinct().all()


	def get_recipes(user_id, title_opt, ingredients, page, per_page):
		# Get the necessary recipe ids from the asked ingredient list
		filteredIngredients = RecipeService.get_recipe_ids_from_filtered_ingredients(ingredients)

		# If we don't find any ingredients we can return an empty list
		if filteredIngredients and len(filteredIngredients) == 0:
			return list()

		# Clean optional title
		title = xstr(title_opt)
		# Prepare recipe title filter
		recipeFilter = Recipe.title.like(f"%{title}%")
		# Start recipe query
		query = Recipe.query.filter(recipeFilter)
		# Filter by user_id if needed
		if (user_id):
			query = query.filter(Recipe.user_id == user_id)
		# If we have ingredient, add additional filter to the initial query
		if filteredIngredients:
			filteredIngredients = list(map(lambda i: i[0], filteredIngredients))
			query = query.filter(Recipe._id.in_(filteredIngredients))

		# Prepare order by
		order_by = Recipe.created_at.desc()
		# Add order by to query
		query = query.order_by(order_by)
		# Run final query with pagination
		paginatedRecipes = query.paginate(page=page, per_page=per_page, error_out=False)

		recipeIdsOnPage = list(map(lambda r: r._id, paginatedRecipes.items))
		ingredientsPerRecipe = {}
		for recipeId in recipeIdsOnPage:
			ingredients = Ingredient.query.filter(Ingredient.recipe_id == recipeId).order_by(Ingredient.name.desc()).all()
			ingredientsPerRecipe[recipeId] = ingredients

		return (paginatedRecipes, ingredientsPerRecipe)


	def insert_recipe(user_id, form_data):
		def toIngredient(recipe_id):
			def fn(ingredient):
				return Ingredient(recipe_id=recipe_id, name=ingredient["name"], amount=ingredient["amount"], measurement=ingredient["measurement"])
			return fn
  
		newRecipe = Recipe(user_id=user_id, title=form_data["title"], prep_time=form_data["prep_time"], cooking_time=form_data["cooking_time"], description=form_data["description"])
  
		db.session.add(newRecipe)
		db.session.commit()
  
		ingredientList = list(map(toIngredient(newRecipe._id), form_data["ingredient_list"]))
		db.session.add_all(ingredientList)
		db.session.commit()

		return None
   