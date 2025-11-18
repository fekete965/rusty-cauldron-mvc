-- migration-06

-- User 2 recipes
INSERT INTO recipes (user_id, title, prep_time, cooking_time, description, deleted) 
VALUES (2, 'Fluffy Pancakes', 10, 15, 
  '1. In a medium bowl, whisk together 1 cup flour, 2 tablespoons sugar, 2 teaspoons baking powder, and 1/2 teaspoon salt. 
  2. In a separate bowl, whisk together 1 cup milk, 1 egg, and 2 tablespoons melted butter. 
  3. Pour the wet ingredients into the dry ingredients and mix until just combined. 
  4. Heat a non-stick pan over medium heat and scoop 1/4 cup of batter for each pancake. 
  5. Cook until small bubbles form on the surface, then flip and cook for an additional 2 minutes. 
  6. Serve hot with syrup and butter.', 0);

INSERT INTO ingredients (recipe_id, name, amount, measurement, deleted) 
VALUES ((SELECT id FROM recipes WHERE title = 'Fluffy Pancakes' AND user_id = 2), 'flour', 1, 'cup', 0),
       ((SELECT id FROM recipes WHERE title = 'Fluffy Pancakes' AND user_id = 2), 'sugar', 2, 'tbs', 0),
       ((SELECT id FROM recipes WHERE title = 'Fluffy Pancakes' AND user_id = 2), 'baking powder', 2, 'tsp', 0),
       ((SELECT id FROM recipes WHERE title = 'Fluffy Pancakes' AND user_id = 2), 'salt', 0.5, 'tsp', 0),
       ((SELECT id FROM recipes WHERE title = 'Fluffy Pancakes' AND user_id = 2), 'milk', 1, 'cup', 0),
       ((SELECT id FROM recipes WHERE title = 'Fluffy Pancakes' AND user_id = 2), 'egg', 1, 'small', 0),
       ((SELECT id FROM recipes WHERE title = 'Fluffy Pancakes' AND user_id = 2), 'butter', 2, 'tbs', 0);

INSERT INTO recipes (user_id, title, prep_time, cooking_time, description, deleted)
VALUES (2, 'Strawberry Shortcake', 30, 30, 'Strawberry Shortcake Recipe:\n\n
1. Preheat oven to 350°F (175°C).\n
2. In a medium bowl, whisk together flour, sugar, baking powder, and salt.\n
3. Cut in butter until mixture resembles coarse crumbs.\n
4. Stir in milk just until mixture forms a soft dough.\n
5. On a lightly floured surface, knead dough by folding and gently pressing dough 10 to 12 times.\n
6. Roll or pat dough to 1/2 inch thickness.\n
7. Cut with 2 1/2 inch biscuit cutter.\n
8. Place on ungreased baking sheet.\n
9. Bake for 12 to 15 minutes or until golden.\n
10. Split biscuits in half.\n
11. Fill with sliced strawberries and whipped cream.\n
12. Replace tops of biscuits.\n
13. Serve immediately.', 0);

INSERT INTO ingredients (recipe_id, name, amount, measurement, deleted)
VALUES ((SELECT id FROM recipes WHERE title = 'Strawberry Shortcake' AND user_id = 2), 'flour', 2, 'cup', 0),
       ((SELECT id FROM recipes WHERE title = 'Strawberry Shortcake' AND user_id = 2), 'sugar', 3, 'tbs', 0),
       ((SELECT id FROM recipes WHERE title = 'Strawberry Shortcake' AND user_id = 2), 'baking powder', 1, 'tsp', 0),
       ((SELECT id FROM recipes WHERE title = 'Strawberry Shortcake' AND user_id = 2), 'salt', 0.25, 'tsp', 0),
       ((SELECT id FROM recipes WHERE title = 'Strawberry Shortcake' AND user_id = 2), 'butter', 0.25, 'cup', 0),
       ((SELECT id FROM recipes WHERE title = 'Strawberry Shortcake' AND user_id = 2), 'milk', 0.25, 'cup', 0),
       ((SELECT id FROM recipes WHERE title = 'Strawberry Shortcake' AND user_id = 2), 'strawberries', 2, 'cup', 0),
       ((SELECT id FROM recipes WHERE title = 'Strawberry Shortcake' AND user_id = 2), 'whipped cream', 1, 'cup', 0);
