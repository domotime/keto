from recipes.models.recipe import Recipe
import json
from django.core import serializers
from django.http import HttpResponse

def export_recipes_to_json(file_path):
    # Get all the recipes
    recipes = Recipe.objects.all()
    # Create a list to store the json data of each recipe
    json_recipes = []
    # Iterate through all the recipes
    for recipe in recipes:
        # Get the json data of each recipe
        json_recipe = json.loads(recipe.to_json())
        # Append the json data to the json_recipes list
        json_recipes.append(json_recipe)

    # Write the json data to a file
    with open(file_path, 'w') as json_file:
        json.dump(json_recipes, json_file, indent=4)

export_recipes_to_json("./export.json")