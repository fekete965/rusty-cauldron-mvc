-- migration-08

-- User 4 recipes
INSERT INTO recipes (user_id, title, prep_time, cooking_time, description)
VALUES (4, 'Vegetarian Chili', 20, 40, 'In a large pot, heat 1 tablespoon of oil over medium heat. Add 1 chopped onion, 1 chopped red pepper, 1 chopped green pepper, and 2 cloves of minced garlic. Cook for 5 minutes, stirring occasionally. 

Add 1 can of diced tomatoes, 1 can of corn, 1 can of black beans, 1 can of kidney beans, 1 tablespoon of chili powder, 1 teaspoon of cumin, and 1/2 teaspoon of salt to the pot. Stir to combine.

Bring the mixture to a boil, then reduce the heat and let it simmer for 30 minutes, stirring occasionally. 

While the chili is cooking, prepare the toppings. Grate 1 cup of cheddar cheese and chop 1/2 cup of fresh cilantro. 

When the chili is done, serve it hot topped with cheese and cilantro.');

INSERT INTO ingredients (recipe_id, name, amount, measurement)
VALUES ((SELECT id FROM recipes WHERE title = 'Vegetarian Chili' AND user_id = 4),'oil', 1, 'tbs'),
       ((SELECT id FROM recipes WHERE title = 'Vegetarian Chili' AND user_id = 4),'onion', 1, 'large'),
       ((SELECT id FROM recipes WHERE title = 'Vegetarian Chili' AND user_id = 4),'red pepper', 1, 'medium'),
       ((SELECT id FROM recipes WHERE title = 'Vegetarian Chili' AND user_id = 4),'green pepper', 1, 'medium'),
       ((SELECT id FROM recipes WHERE title = 'Vegetarian Chili' AND user_id = 4),'garlic', 2, 'cl'),
       ((SELECT id FROM recipes WHERE title = 'Vegetarian Chili' AND user_id = 4),'diced tomatoes', 1, 'can'),
       ((SELECT id FROM recipes WHERE title = 'Vegetarian Chili' AND user_id = 4),'corn', 1, 'can'),
       ((SELECT id FROM recipes WHERE title = 'Vegetarian Chili' AND user_id = 4),'black beans', 1, 'can'),
       ((SELECT id FROM recipes WHERE title = 'Vegetarian Chili' AND user_id = 4),'kidney beans', 1, 'can'),
       ((SELECT id FROM recipes WHERE title = 'Vegetarian Chili' AND user_id = 4),'chili powder', 1, 'tbs'),
       ((SELECT id FROM recipes WHERE title = 'Vegetarian Chili' AND user_id = 4),'cumin', 1, 'tsp'),
       ((SELECT id FROM recipes WHERE title = 'Vegetarian Chili' AND user_id = 4),'salt', 0.5, 'tsp'),
       ((SELECT id FROM recipes WHERE title = 'Vegetarian Chili' AND user_id = 4),'cheddar cheese', 1, 'cup'),
       ((SELECT id FROM recipes WHERE title = 'Vegetarian Chili' AND user_id = 4),'fresh cilantro', 0.5, 'cup');

INSERT INTO recipes (user_id, title, prep_time, cooking_time, description)
VALUES (4, 'Tomato and Basil Pasta', 15, 20, 
'1. Cook 1 pound of spaghetti according to package instructions in a large pot of salted water. 
 2. Meanwhile, heat 1/4 cup of olive oil in a large skillet over medium heat. Add 4 cloves of minced garlic and cook until fragrant, about 1 minute. 
 3. Stir in 4 cups of chopped fresh tomatoes, 1/2 teaspoon of salt, and 1/4 teaspoon of black pepper. Cook until the tomatoes have broken down, about 10 minutes. 
 4. Stir in 1/2 cup of fresh basil leaves and cook for another 1-2 minutes. 
 5. Drain the pasta and return it to the pot. Toss the pasta with the tomato sauce until well combined. Serve immediately, topped with grated Parmesan cheese and extra basil leaves, if desired. Enjoy!');
 
INSERT INTO ingredients (recipe_id, name, amount, measurement)
VALUES (1, (SELECT id FROM recipes WHERE title = 'Tomato and Basil Pasta' AND user_id = 4), 'spaghetti', 1, 'lb'),
       (1, (SELECT id FROM recipes WHERE title = 'Tomato and Basil Pasta' AND user_id = 4), 'olive oil', 0.25, 'cup'),
       (1, (SELECT id FROM recipes WHERE title = 'Tomato and Basil Pasta' AND user_id = 4), 'garlic', 4, 'cloves'),
       (1, (SELECT id FROM recipes WHERE title = 'Tomato and Basil Pasta' AND user_id = 4), 'tomatoes', 4, 'cups'),
       (1, (SELECT id FROM recipes WHERE title = 'Tomato and Basil Pasta' AND user_id = 4), 'salt', 0.5, 'tsp'),
       (1, (SELECT id FROM recipes WHERE title = 'Tomato and Basil Pasta' AND user_id = 4), 'black pepper', 0.25, 'tsp'),
       (1, (SELECT id FROM recipes WHERE title = 'Tomato and Basil Pasta' AND user_id = 4), 'basil leaves', 0.5, 'cup'),
       (1, (SELECT id FROM recipes WHERE title = 'Tomato and Basil Pasta' AND user_id = 4), 'Parmesan cheese', 250, 'gramm');
