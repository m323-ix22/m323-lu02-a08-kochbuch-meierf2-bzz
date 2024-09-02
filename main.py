"""Kochbuch"""

import json


def adjust_recipe(my_recipe, num_people):
    factor = num_people / my_recipe['servings']
    adjusted_ingredients = {ingredient: amount * factor for ingredient, amount in my_recipe['ingredients'].items()}
    adjusted_recipe = {
        'title': my_recipe['title'],
        'ingredients': adjusted_ingredients,
        'servings': num_people
    }

    return adjusted_recipe


def load_recipe(my_recipe_json):
    return json.loads(my_recipe_json)


if __name__ == '__main__':
    recipe_json = ('{"title": "Spaghetti Bolognese", "ingredients": '
                   '{"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}')
    recipe = load_recipe(recipe_json)
    new_recipe = adjust_recipe(recipe, 2)
    print(f'Original recipe: {recipe}')
    print(f'Adjusted recipe: {new_recipe}')
