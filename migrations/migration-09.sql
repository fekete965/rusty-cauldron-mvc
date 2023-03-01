-- migration-09

-- User 5 recipes
INSERT INTO recipes (user_id, title, prep_time, cooking_time, description, deleted)
VALUES (5, 'Lemon Garlic Chicken', 15, 35, 'Lemon Garlic Chicken is a simple, delicious, and healthy dish that can be enjoyed any night of the week. Here is the full making process:
1. In a large bowl, mix together lemon juice, minced garlic, olive oil, salt, pepper, and dried oregano.
2. Add chicken breasts to the marinade, making sure they are well coated. Cover and refrigerate for at least 30 minutes or up to 2 hours.
3. Preheat the oven to 400°F (200°C). Line a baking sheet with parchment paper.
4. Remove the chicken from the marinade, allowing any excess to drip off, and place it on the prepared baking sheet.
5. Roast the chicken for 25-30 minutes or until fully cooked through and golden brown.
6. Serve the chicken hot with a squeeze of lemon juice and a sprinkle of chopped parsley.
Enjoy your delicious Lemon Garlic Chicken!', 0);

INSERT INTO ingredients (recipe_id, name, amount, measurement)
VALUES ((SELECT id FROM recipes WHERE title = 'Lemon Garlic Chicken' AND user_id = 5), 'Lemon juice', 1, 'large'),
       ((SELECT id FROM recipes WHERE title = 'Lemon Garlic Chicken' AND user_id = 5), 'Garlic cloves', 4, 'medium'),
       ((SELECT id FROM recipes WHERE title = 'Lemon Garlic Chicken' AND user_id = 5), 'Olive oil', 2, 'tbs'),
       ((SELECT id FROM recipes WHERE title = 'Lemon Garlic Chicken' AND user_id = 5), 'Salt', 1, 'tsp'),
       ((SELECT id FROM recipes WHERE title = 'Lemon Garlic Chicken' AND user_id = 5), 'Pepper', 1, 'tsp'),
       ((SELECT id FROM recipes WHERE title = 'Lemon Garlic Chicken' AND user_id = 5), 'Dried oregano', 1, 'tsp'),
       ((SELECT id FROM recipes WHERE title = 'Lemon Garlic Chicken' AND user_id = 5), 'Chicken breasts', 4, 'large'),
       ((SELECT id FROM recipes WHERE title = 'Lemon Garlic Chicken' AND user_id = 5), 'Lemon juice', 1, 'large'),
       ((SELECT id FROM recipes WHERE title = 'Lemon Garlic Chicken' AND user_id = 5), 'Parsley', 1, 'large');

INSERT INTO recipes (user_id, title, prep_time, cooking_time, description, deleted)
VALUES (5, 'Classic Macaroni and Cheese', 20, 30, 'To make this delicious classic Macaroni and Cheese, follow these steps:
1. Cook macaroni according to package directions until al dente. Drain and set aside.
2. In a separate saucepan, melt butter over medium heat. Stir in flour until smooth. Gradually add milk, whisking constantly until the mixture thickens, about 5 minutes.
3. Stir in grated cheddar cheese until melted. Season with salt and pepper to taste.
4. Combine cooked macaroni with the cheese sauce and pour into a baking dish. Top with breadcrumbs and bake at 350°F for 20 minutes or until the top is golden brown.
5. Serve hot and enjoy!', 0);

INSERT INTO ingredients (recipe_id, name, amount, measurement)
VALUES ((SELECT id FROM recipes WHERE user_id = 5 AND title = 'Classic Macaroni and Cheese'), 'macaroni', 1, 'lb'),
       ((SELECT id FROM recipes WHERE user_id = 5 AND title = 'Classic Macaroni and Cheese'), 'butter', 2, 'tbs'),
       ((SELECT id FROM recipes WHERE user_id = 5 AND title = 'Classic Macaroni and Cheese'), 'flour', 1, 'tbs'),
       ((SELECT id FROM recipes WHERE user_id = 5 AND title = 'Classic Macaroni and Cheese'), 'milk', 2, 'cup'),
       ((SELECT id FROM recipes WHERE user_id = 5 AND title = 'Classic Macaroni and Cheese'), 'cheddar cheese', 2, 'cup'),
       ((SELECT id FROM recipes WHERE user_id = 5 AND title = 'Classic Macaroni and Cheese'), 'salt', 0.5, 'tsp'),
       ((SELECT id FROM recipes WHERE user_id = 5 AND title = 'Classic Macaroni and Cheese'), 'pepper', 0.5, 'tsp'),
       ((SELECT id FROM recipes WHERE user_id = 5 AND title = 'Classic Macaroni and Cheese'), 'breadcrumbs', 0.5, 'cup');
