from tables.recipes import Recipe
from utils.main import xstr
from persist import db

class RecipeService():
  def get_recipes(titleOpt, ingredients, page, per_page):
    title = xstr(titleOpt)
    
    query = Recipe.title.like(f"%{title}%")
    order_by = Recipe.created_at.desc()
    
    return Recipe.query.filter(query).order_by(order_by).paginate(page=page,per_page=per_page,error_out=False)
