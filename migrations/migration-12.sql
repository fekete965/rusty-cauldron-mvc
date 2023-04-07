-- migration-012

-- User 8 recipes
INSERT INTO recipes (user_id, title, prep_time, cooking_time, description, deleted)
VALUES (8, 'Crispy Baked Chicken', 10, 25,
'1. Preheat oven to 400°F (200°C).

In a shallow dish, mix together 1 cup of panko breadcrumbs, 1/4 cup of grated Parmesan cheese, 1/2 teaspoon of garlic powder, 1/2 teaspoon of paprika, 1/2 teaspoon of dried thyme, 1/2 teaspoon of salt, and 1/4 teaspoon of black pepper.
In another shallow dish, whisk together 2 eggs.
Dip 4 boneless, skinless chicken breasts into the egg mixture, then coat with the breadcrumb mixture. Place the chicken on a baking sheet lined with parchment paper.
Bake for 20-25 minutes, or until the chicken is cooked through and the coating is golden brown and crispy.
Serve immediately, garnished with fresh herbs and lemon wedges, if desired. Enjoy!', 0);

INSERT INTO ingredients (recipe_id, name, amount, measurement, deleted)
VALUES ((SELECT id FROM recipes WHERE title = 'Crispy Baked Chicken' AND user_id = 8), 'panko breadcrumbs', 1, 'cup', 0),
       ((SELECT id FROM recipes WHERE title = 'Crispy Baked Chicken' AND user_id = 8), 'Parmesan cheese', 0.25, 'cup', 0),
       ((SELECT id FROM recipes WHERE title = 'Crispy Baked Chicken' AND user_id = 8), 'garlic powder', 0.5, 'tsp', 0),
       ((SELECT id FROM recipes WHERE title = 'Crispy Baked Chicken' AND user_id = 8), 'paprika', 0.5, 'tsp', 0),
       ((SELECT id FROM recipes WHERE title = 'Crispy Baked Chicken' AND user_id = 8), 'dried thyme', 0.5, 'tsp', 0),
       ((SELECT id FROM recipes WHERE title = 'Crispy Baked Chicken' AND user_id = 8), 'salt', 0.5, 'tsp', 0),
       ((SELECT id FROM recipes WHERE title = 'Crispy Baked Chicken' AND user_id = 8), 'black pepper', 0.25, 'tsp', 0),
       ((SELECT id FROM recipes WHERE title = 'Crispy Baked Chicken' AND user_id = 8), 'eggs', 2, 'medium', 0),
       ((SELECT id FROM recipes WHERE title = 'Crispy Baked Chicken' AND user_id = 8), 'boneless, skinless chicken breasts', 4, 'medium', 0),
       ((SELECT id FROM recipes WHERE title = 'Crispy Baked Chicken' AND user_id = 8), 'fresh herbs', 25, 'gramm', 0),
       ((SELECT id FROM recipes WHERE title = 'Crispy Baked Chicken' AND user_id = 8), 'lemon wedges', 4, 'medium', 0);

INSERT INTO recipes (user_id, title, prep_time, cooking_time, description, deleted)
VALUES (8, "Garlic Shrimp Linguine", 10, 15,
"1. Cook 8 oz of linguine according to package instructions in a large pot of salted water.

Meanwhile, heat 1/4 cup of butter and 2 tbsp of olive oil in a large skillet over medium heat. Add 5 cloves of minced garlic and cook until fragrant, about 1 minute.
Add 1 lb of raw shrimp, peeled and deveined, and cook until they turn pink, about 3-4 minutes.
Add 1/4 cup of dry white wine, 1/4 cup of chicken broth, and 1/4 tsp of red pepper flakes. Bring to a simmer and cook for 1-2 minutes until the liquid has reduced by half.
Drain the pasta and add it to the skillet. Toss with the sauce until the pasta is coated.
Season with salt and pepper to taste. Serve immediately, garnished with chopped parsley and lemon wedges. Enjoy!", 0);

INSERT INTO ingredients (recipe_id, name, amount, measurement, deleted)
VALUES ((SELECT id FROM recipes WHERE title = "Garlic Shrimp Linguine" AND user_id = 8), "linguine", 8, "oz", 0),
       ((SELECT id FROM recipes WHERE title = "Garlic Shrimp Linguine" AND user_id = 8), "butter", 0.25, "cup", 0),
       ((SELECT id FROM recipes WHERE title = "Garlic Shrimp Linguine" AND user_id = 8), "olive oil", 2, "tbsp", 0),
       ((SELECT id FROM recipes WHERE title = "Garlic Shrimp Linguine" AND user_id = 8), "garlic", 5, "cloves", 0),
       ((SELECT id FROM recipes WHERE title = "Garlic Shrimp Linguine" AND user_id = 8), "shrimp", 1, "lb", 0),
       ((SELECT id FROM recipes WHERE title = "Garlic Shrimp Linguine" AND user_id = 8), "dry white wine", 0.25, "cup", 0),
       ((SELECT id FROM recipes WHERE title = "Garlic Shrimp Linguine" AND user_id = 8), "chicken broth", 0.25, "cup", 0),
       ((SELECT id FROM recipes WHERE title = "Garlic Shrimp Linguine" AND user_id = 8), "red pepper flakes", 0.25, "tsp", 0),
       ((SELECT id FROM recipes WHERE title = "Garlic Shrimp Linguine" AND user_id = 8), "salt", 0.25, "tsp", 0),
       ((SELECT id FROM recipes WHERE title = "Garlic Shrimp Linguine" AND user_id = 8), "pepper", 0.25, "tsp", 0),
       ((SELECT id FROM recipes WHERE title = "Garlic Shrimp Linguine" AND user_id = 8), "parsley", 1, "tsp", 0),
       ((SELECT id FROM recipes WHERE title = "Garlic Shrimp Linguine" AND user_id = 8), "lemon wedges", 4, 'medium', 0);
