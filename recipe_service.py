from sqlalchemy import func
from tables.ingredients import Ingredient
from tables.recipes import Recipe
from utils.main import xstr
from app import db

class RecipeService():
	# Get optional recipe ids from ingredients
	def get_recipe_ids_from_filtered_ingredients(ingredients):
		if len(ingredients) == 0:
			return None
		filtered_ingredient_filter = [Ingredient.name.like(f"%{ingredient}%") for ingredient in ingredients]
		return Ingredient.query.with_entities(Ingredient.recipe_id).filter(*filtered_ingredient_filter).distinct().all()


	def get_recipes(user_id, title_opt, ingredients, page, per_page):
		# Get the necessary recipe ids from the asked ingredient list
		filtered_ingredients = RecipeService.get_recipe_ids_from_filtered_ingredients(ingredients)

		# If we don't find any ingredients we can return an empty list
		if filtered_ingredients and len(filtered_ingredients) == 0:
			return list()

		# Clean optional title
		title = xstr(title_opt)
		# Prepare recipe title filter
		title_filter = Recipe.title.like(f"%{title}%")
		is_active_filter = Recipe.deleted == False
		# Start recipe query
		query = Recipe.query.filter(title_filter, is_active_filter)
		# Filter by user_id if needed
		if (user_id):
			query = query.filter(Recipe.user_id == user_id)
		# If we have ingredient, add additional filter to the initial query
		if filtered_ingredients:
			filtered_ingredients = list(map(lambda i: i[0], filtered_ingredients))
			query = query.filter(Recipe._id.in_(filtered_ingredients))

		# Prepare order by
		order_by = Recipe.created_at.desc()
		# Add order by to query
		query = query.order_by(order_by)
		# Run final query with pagination
		paginated_recipes = query.paginate(page=page, per_page=per_page, error_out=False)

		recipe_ids_on_page = list(map(lambda r: r._id, paginated_recipes.items))
		ingredients_per_recipe = {}
		for recipeId in recipe_ids_on_page:
			ingredients = Ingredient.\
				query.\
				filter(Ingredient.recipe_id == recipeId).\
				order_by(Ingredient.name.desc()).\
				all()
			ingredients_per_recipe[recipeId] = ingredients

		return (paginated_recipes, ingredients_per_recipe)


	def insert_recipe(user_id, title, prep_time, cooking_time, ingredient_list, description):
		def to_ingredient(recipe_id):
			def fn(ingredient):
				return Ingredient(
					recipe_id=recipe_id,
					name=ingredient["name"],
					amount=ingredient["amount"],
					measurement=ingredient["measurement"]
				)
			return fn
  
		newRecipe = Recipe(
			user_id=user_id,
			title=title,
			prep_time=prep_time,
			cooking_time=cooking_time,
			description=description,
		)
  
		db.session.add(newRecipe)
		db.session.commit()
  
		new_ingredients = list(map(to_ingredient(newRecipe._id), ingredient_list))
		db.session.add_all(new_ingredients)
		db.session.commit()

		return True


	def mark_recipe_as_deleted(user_id, recipe_id):
		db.session.query(Recipe).\
			filter(Recipe.user_id == user_id, Recipe._id == recipe_id).\
			update({ "deleted": True, "updated_at": func.now() })
		db.session.commit()

		return True

   
	def find_recipe_by_id(recipe_id):
		recipe = Recipe.query.filter(Recipe._id == recipe_id).first()
		ingredients = Ingredient.query.filter(Ingredient.recipe_id == recipe._id).all()

		return (recipe, ingredients)
