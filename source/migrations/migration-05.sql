-- migration-05

-- User 1 recipes
INSERT INTO recipes (user_id, title, prep_time, cooking_time, description, deleted)
VALUES (1, 'Butterbeer', 15, 20, '
  In a large bowl, whisk together the flour, sugar, baking powder, salt, and cinnamon. In a separate bowl, whisk together the milk, melted butter, egg, and vanilla extract. Pour the wet mixture into the dry mixture and stir until just combined. 
  Heat a large non-stick pan or griddle over medium heat. Using a 1/4 cup measure, pour batter onto the hot pan. Cook until small bubbles form on the surface of the pancakes, then flip and cook until both sides are golden brown.
  In a small saucepan, melt the butter, heavy cream, and brown sugar together. Once melted, remove from heat and whisk in the vanilla extract. Serve pancakes hot with the warm butterbeer syrup and whipped cream on top.', 0);

INSERT INTO ingredients (recipe_id, name, amount, measurement, deleted)
VALUES ((SELECT id FROM recipes WHERE title = 'Butterbeer' AND user_id = 1), 'flour', 2, 'cup', 0),
       ((SELECT id FROM recipes WHERE title = 'Butterbeer' AND user_id = 1), 'sugar', 2, 'tbs', 0),
       ((SELECT id FROM recipes WHERE title = 'Butterbeer' AND user_id = 1), 'baking powder', 1.5, 'tsp', 0),
       ((SELECT id FROM recipes WHERE title = 'Butterbeer' AND user_id = 1), 'salt', 0.5, 'tsp', 0),
       ((SELECT id FROM recipes WHERE title = 'Butterbeer' AND user_id = 1), 'cinnamon', 1, 'tsp', 0),
       ((SELECT id FROM recipes WHERE title = 'Butterbeer' AND user_id = 1), 'milk', 1, 'cup', 0),
       ((SELECT id FROM recipes WHERE title = 'Butterbeer' AND user_id = 1), 'butter, melted', 4, 'tbs', 0),
       ((SELECT id FROM recipes WHERE title = 'Butterbeer' AND user_id = 1), 'egg', 1, 'large', 0),
       ((SELECT id FROM recipes WHERE title = 'Butterbeer' AND user_id = 1), 'vanilla extract', 1, 'tsp', 0),
       ((SELECT id FROM recipes WHERE title = 'Butterbeer' AND user_id = 1), 'butter', 4, 'tbs', 0),
       ((SELECT id FROM recipes WHERE title = 'Butterbeer' AND user_id = 1), 'heavy cream', 0.25, 'cup', 0),
       ((SELECT id FROM recipes WHERE title = 'Butterbeer' AND user_id = 1), 'brown sugar', 0.25, 'cup', 0),
       ((SELECT id FROM recipes WHERE title = 'Butterbeer' AND user_id = 1), 'whipped cream', 1, 'cup', 0);

INSERT INTO recipes (user_id, title, prep_time, cooking_time, description, deleted)
VALUES (1, 'Pumpkin Pasties', 30, 45, 'A sweet pastry filled with pumpkin filling - Roll out pie dough and cut into circles. Mix pumpkin puree, sugar, cinnamon, nutmeg and ginger in a bowl. Spoon the mixture onto one half of each dough circle, fold the other half over and crimp the edges to seal. Bake until golden brown and serve!', 0);

INSERT INTO ingredients (recipe_id, name, amount, measurement, deleted) 
VALUES ((SELECT id FROM recipes WHERE title = 'Pumpkin Pasties' AND user_id = 1), 'Pie dough', 1, 'package', 0),
       ((SELECT id FROM recipes WHERE title = 'Pumpkin Pasties' AND user_id = 1), 'Pumpkin puree', 2, 'cups', 0),
       ((SELECT id FROM recipes WHERE title = 'Pumpkin Pasties' AND user_id = 1), 'Sugar', 1, 'cup', 0),
       ((SELECT id FROM recipes WHERE title = 'Pumpkin Pasties' AND user_id = 1), 'Cinnamon', 1, 'tsp', 0),
       ((SELECT id FROM recipes WHERE title = 'Pumpkin Pasties' AND user_id = 1), 'Nutmeg', 0.5, 'tsp', 0),
       ((SELECT id FROM recipes WHERE title = 'Pumpkin Pasties' AND user_id = 1), 'Ginger', 0.5, 'tsp', 0);
