-- migration-011

-- User 7 recipes
INSERT INTO recipes (user_id, title, prep_time, cooking_time, description, deleted)
VALUES (7, 'Creamy Garlic Chicken', 10, 25, 'This delicious creamy garlic chicken recipe is easy to make and perfect for a weeknight dinner. Here''s how to make it:\n\n1. Heat a tablespoon of olive oil in a large skillet over medium heat.\n2. Add boneless, skinless chicken breasts to the skillet and cook until golden brown on both sides.\n3. Remove the chicken from the skillet and set it aside on a plate.\n4. Add chopped garlic to the same skillet and cook for 1-2 minutes until fragrant.\n5. Add heavy cream, chicken broth, and grated Parmesan cheese to the skillet and whisk until the sauce is smooth.\n6. Return the chicken to the skillet and simmer until the chicken is cooked through and the sauce has thickened.\n7. Season the chicken with salt and pepper to taste, and serve with your favorite side dish.\n\nEnjoy!', 0);

INSERT INTO ingredients (recipe_id, name, amount, measurement, deleted)
VALUES
      ((SELECT id FROM recipes WHERE title = 'Creamy Garlic Chicken' AND user_id = 7), 'Boneless, skinless chicken breasts', 4, 'medium', 0),
      ((SELECT id FROM recipes WHERE title = 'Creamy Garlic Chicken' AND user_id = 7), 'Olive oil', 1, 'tbsp', 0),
      ((SELECT id FROM recipes WHERE title = 'Creamy Garlic Chicken' AND user_id = 7), 'Garlic', 4, 'cloves', 0),
      ((SELECT id FROM recipes WHERE title = 'Creamy Garlic Chicken' AND user_id = 7), 'Heavy cream', 1, 'cup', 0),
      ((SELECT id FROM recipes WHERE title = 'Creamy Garlic Chicken' AND user_id = 7), 'Chicken broth', 1, 'cup', 0),
      ((SELECT id FROM recipes WHERE title = 'Creamy Garlic Chicken' AND user_id = 7), 'Grated Parmesan cheese', 1, 'cup', 0);

INSERT INTO recipes (user_id, title, prep_time, cooking_time, description, deleted)
VALUES (7, 'Mushroom Risotto', 10, 30,
'1. In a medium saucepan, bring 4 cups of vegetable broth to a simmer over medium heat.

In a large saucepan, melt 2 tablespoons of butter over medium heat. Add 1 chopped onion and cook until softened, about 5 minutes.
Add 2 cups of sliced mushrooms and cook until tender and browned, about 8-10 minutes.
Add 1 1/2 cups of Arborio rice and stir to coat with the mushroom mixture.
Add 1/2 cup of white wine and stir until absorbed.
Add 1/2 cup of the simmering vegetable broth and stir until absorbed.
Continue adding the broth, 1/2 cup at a time, stirring constantly and allowing each addition to be absorbed before adding the next, until the rice is tender and the mixture is creamy, about 20-25 minutes.
Stir in 1/2 cup of grated Parmesan cheese and 2 tablespoons of chopped fresh parsley.
Season with salt and pepper to taste. Serve immediately, garnished with additional Parmesan cheese and parsley, if desired. Enjoy!', 0);

INSERT INTO ingredients (recipe_id, name, amount, measurement, deleted)
VALUES 
      ((SELECT id FROM recipes WHERE title = 'Mushroom Risotto' AND user_id = 7), 'vegetable broth', 4, 'cups', 0),
      ((SELECT id FROM recipes WHERE title = 'Mushroom Risotto' AND user_id = 7), 'butter', 2, 'tbsp', 0),
      ((SELECT id FROM recipes WHERE title = 'Mushroom Risotto' AND user_id = 7), 'onion', 1, 'large', 0),
      ((SELECT id FROM recipes WHERE title = 'Mushroom Risotto' AND user_id = 7), 'mushrooms', 2, 'cups', 0),
      ((SELECT id FROM recipes WHERE title = 'Mushroom Risotto' AND user_id = 7), 'Arborio rice', 1.5, 'cups', 0),
      ((SELECT id FROM recipes WHERE title = 'Mushroom Risotto' AND user_id = 7), 'white wine', 0.5, 'cup', 0),
      ((SELECT id FROM recipes WHERE title = 'Mushroom Risotto' AND user_id = 7), 'Parmesan cheese', 0.5, 'cup', 0),
      ((SELECT id FROM recipes WHERE title = 'Mushroom Risotto' AND user_id = 7), 'fresh parsley', 2, 'tbsp', 0);
