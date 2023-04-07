-- migration-010

-- User 6 recipes
INSERT INTO recipes (user_id, title, prep_time, cooking_time, description, deleted)
VALUES (6, 'Spicy Chicken Stir-Fry', 10, 15, 'This spicy chicken stir-fry is a quick and easy weeknight dinner that packs a punch of flavor. To make this dish, start by marinating thinly sliced chicken breast in a mixture of soy sauce, sesame oil, and cornstarch. While the chicken is marinating, chop up your vegetables of choice and make a sauce using soy sauce, honey, garlic, ginger, and chili paste. When everything is prepped, stir-fry the chicken in a hot wok or skillet until it's cooked through, then add the veggies and sauce and cook until the veggies are tender-crisp. Serve over rice or noodles for a satisfying meal that's ready in under 30 minutes.', 0);

INSERT INTO ingredients (recipe_id, name, amount, measurement, deleted)
VALUES ((SELECT id FROM recipes WHERE title = 'Spicy Chicken Stir-Fry' AND user_id = 6), 'chicken breast', 1, 'lb', 0),
       ((SELECT id FROM recipes WHERE title = 'Spicy Chicken Stir-Fry' AND user_id = 6), 'soy sauce', 1, 'tbsp', 0),
       ((SELECT id FROM recipes WHERE title = 'Spicy Chicken Stir-Fry' AND user_id = 6), 'sesame oil', 1, 'tsp', 0),
       ((SELECT id FROM recipes WHERE title = 'Spicy Chicken Stir-Fry' AND user_id = 6), 'cornstarch', 1, 'tbsp', 0),
       ((SELECT id FROM recipes WHERE title = 'Spicy Chicken Stir-Fry' AND user_id = 6), 'garlic', 2, 'cloves', 0),
       ((SELECT id FROM recipes WHERE title = 'Spicy Chicken Stir-Fry' AND user_id = 6), 'ginger', 1, 'inch', 0),
       ((SELECT id FROM recipes WHERE title = 'Spicy Chicken Stir-Fry' AND user_id = 6), 'honey', 1, 'tbsp', 0),
       ((SELECT id FROM recipes WHERE title = 'Spicy Chicken Stir-Fry' AND user_id = 6), 'chili paste', 1, 'tbsp', 0),
       ((SELECT id FROM recipes WHERE title = 'Spicy Chicken Stir-Fry' AND user_id = 6), 'red bell pepper', 1, 'large', 0),
       ((SELECT id FROM recipes WHERE title = 'Spicy Chicken Stir-Fry' AND user_id = 6), 'yellow onion', 1, 'medium', 0),
       ((SELECT id FROM recipes WHERE title = 'Spicy Chicken Stir-Fry' AND user_id = 6), 'green onion', 2, 'stalks', 0),
       ((SELECT id FROM recipes WHERE title = 'Spicy Chicken Stir-Fry' AND user_id = 6), 'vegetable oil', 2, 'tbsp', 0),
       ((SELECT id FROM recipes WHERE title = 'Spicy Chicken Stir-Fry' AND user_id = 6), 'salt', 1, 'tsp', 0),
       ((SELECT id FROM recipes WHERE title = 'Spicy Chicken Stir-Fry' AND user_id = 6), 'black pepper', 1, 'tsp', 0);

INSERT INTO recipes (user_id, title, prep_time, cooking_time, description, deleted)
VALUES (6, "Spicy Shrimp Stir Fry", 10, 15, "This Spicy Shrimp Stir Fry recipe is loaded with juicy shrimp, crisp-tender veggies, and a simple homemade stir fry sauce. It's easy to make and ready in just 25 minutes! To make this delicious dish, follow these steps:

1. In a small bowl, whisk together the stir-fry sauce ingredients: soy sauce, hoisin sauce, honey, and cornstarch. Set aside.
2. Heat a large wok or skillet over high heat. Add the oil and swirl to coat.
3. Add the shrimp to the wok and stir-fry for 2-3 minutes, until they are pink and opaque. Remove the shrimp from the wok and set aside.
4. Add the garlic, ginger, and red pepper flakes to the wok and stir-fry for 30 seconds, until fragrant.
5. Add the vegetables to the wok and stir-fry for 2-3 minutes, until they are tender-crisp.
6. Return the shrimp to the wok and pour the stir-fry sauce over everything. Stir-fry for 1-2 minutes, until the sauce thickens and everything is heated through.
7. Serve over rice or noodles and enjoy!", 0);

INSERT INTO ingredients (recipe_id, name, amount, measurement) VALUES
((SELECT id FROM recipes WHERE title = 'Spicy Shrimp Stir Fry' AND user_id = 6), "Shrimp", 1, "lb", 0),
((SELECT id FROM recipes WHERE title = 'Spicy Shrimp Stir Fry' AND user_id = 6), "Soy Sauce", 3, "tbsp", 0),
((SELECT id FROM recipes WHERE title = 'Spicy Shrimp Stir Fry' AND user_id = 6), "Hoisin Sauce", 2, "tbsp", 0),
((SELECT id FROM recipes WHERE title = 'Spicy Shrimp Stir Fry' AND user_id = 6), "Honey", 2, "tbsp", 0),
((SELECT id FROM recipes WHERE title = 'Spicy Shrimp Stir Fry' AND user_id = 6), "Cornstarch", 1, "tbsp", 0),
((SELECT id FROM recipes WHERE title = 'Spicy Shrimp Stir Fry' AND user_id = 6), "Garlic", 3, "cloves", 0),
((SELECT id FROM recipes WHERE title = 'Spicy Shrimp Stir Fry' AND user_id = 6), "Ginger", 1, "tbsp", 0),
((SELECT id FROM recipes WHERE title = 'Spicy Shrimp Stir Fry' AND user_id = 6), "Red Pepper Flakes", 1, "tsp", 0),
((SELECT id FROM recipes WHERE title = 'Spicy Shrimp Stir Fry' AND user_id = 6), "Broccoli", 2, "cups", 0),
((SELECT id FROM recipes WHERE title = 'Spicy Shrimp Stir Fry' AND user_id = 6), "Bell Peppers", 2, "cups", 0),
((SELECT id FROM recipes WHERE title = 'Spicy Shrimp Stir Fry' AND user_id = 6), "Onion", 1, "medium", 0),
((SELECT id FROM recipes WHERE title = 'Spicy Shrimp Stir Fry' AND user_id = 6), "Oil", 2, "tbsp", 0);
