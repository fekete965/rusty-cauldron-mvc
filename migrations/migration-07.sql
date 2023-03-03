-- migration-07

-- User 3 recipes
INSERT INTO recipes (user_id, title, prep_time, cooking_time, description)
VALUES (3, 'Vegetable Stir Fry', 10, 15, '1. Chop up 2 bell peppers, 2 carrots, and 1 onion into bite-sized pieces. 2. In a pan, heat 1 tbsp of oil over medium heat. 3. Add the chopped vegetables to the pan and stir fry for 10-15 minutes until they are cooked through. 4. Serve the stir fry with rice or noodles.');

INSERT INTO ingredients (recipe_id, name, amount, measurement) 
VALUES ((SELECT id FROM recipes WHERE title = 'Vegetable Stir Fry' AND user_id = 3), 'Bell Pepper', 2, 'medium'),
       ((SELECT id FROM recipes WHERE title = 'Vegetable Stir Fry' AND user_id = 3), 'Carrot', 2, 'medium'),
       ((SELECT id FROM recipes WHERE title = 'Vegetable Stir Fry' AND user_id = 3), 'Onion', 1, 'medium'),
       ((SELECT id FROM recipes WHERE title = 'Vegetable Stir Fry' AND user_id = 3), 'Oil', 1, 'tbsp');

INSERT INTO recipes(user_id, title, prep_time, cooking_time, description)
VALUES (3, 'Tomato Pasta with Grilled Chicken', 15, 20, 'In a large saucepan, heat olive oil over medium heat. Add garlic and onion and cook until onion is soft and translucent, about 5 minutes. Add diced tomatoes, dried basil, dried oregano, salt, and pepper. Cook for 10 minutes until the sauce has thickened. Cook pasta according to package instructions and drain. In a separate pan, grill chicken breasts until cooked through. Serve the pasta topped with the tomato sauce and chicken. Enjoy!');

INSERT INTO ingredients (recipe_id, name, amount, measurement) 
VALUES ((SELECT id FROM recipes WHERE title = 'Tomato Pasta with Grilled Chicken' AND user_id = 3), 'olive oil', 2, 'tbs'),
       ((SELECT id FROM recipes WHERE title = 'Tomato Pasta with Grilled Chicken' AND user_id = 3), 'garlic cloves', 2, 'large'),
       ((SELECT id FROM recipes WHERE title = 'Tomato Pasta with Grilled Chicken' AND user_id = 3), 'onion', 1, 'medium'),
       ((SELECT id FROM recipes WHERE title = 'Tomato Pasta with Grilled Chicken' AND user_id = 3), 'diced tomatoes', 28, 'oz'),
       ((SELECT id FROM recipes WHERE title = 'Tomato Pasta with Grilled Chicken' AND user_id = 3), 'dried basil', 1, 'tbs'),
       ((SELECT id FROM recipes WHERE title = 'Tomato Pasta with Grilled Chicken' AND user_id = 3), 'dried oregano', 1, 'tbs'),
       ((SELECT id FROM recipes WHERE title = 'Tomato Pasta with Grilled Chicken' AND user_id = 3), 'salt', 1, 'tsp'),
       ((SELECT id FROM recipes WHERE title = 'Tomato Pasta with Grilled Chicken' AND user_id = 3), 'pepper', 1, 'tsp'),
       ((SELECT id FROM recipes WHERE title = 'Tomato Pasta with Grilled Chicken' AND user_id = 3), 'pasta', 8, 'oz'),
       ((SELECT id FROM recipes WHERE title = 'Tomato Pasta with Grilled Chicken' AND user_id = 3), 'chicken breasts', 2, 'large');

