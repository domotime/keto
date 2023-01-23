import os
import openai

openai.organization = "org-6oEWKOYBDy8lAtQVU7rLDb2m"
openai.api_key = "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"
openai.Model.list()

from recipes.models.tag import Tag
from recipes.models.recipe import Recipe

from django.shortcuts import render
from random import sample
from recipes.models.recipe import Recipe
from recipes.models.tag import Tag

def random_recipes(tag_name):
    tag = Tag.objects.get(name=tag_name)
    recipes = Recipe.objects.filter(tags=tag)[:30]
    return recipes
    if recipes.count() >= 30:
        return sample(recipes, 30)
    else:
        return recipes

import json

to_save = {'recipes': []}

def save_json():
    global to_save
    with open('json_recipes/recipes.json', 'w') as fp:
        json.dump(to_save, fp)


def generate_recipes_from_tag(tag):
    global openai
    recipes = random_recipes(tag)

    global to_save

    recipe: Recipe
    for recipe in recipes:
        # create a completion
        try:
            completion = openai.Completion.create(engine="text-davinci-003", prompt=\
            ("Scrivi una ricetta in italiano di " + recipe.instructions), max_tokens=2000)

            title = openai.Completion.create(engine="text-davinci-003", prompt=\
                ("Traduci in italiano " + recipe.name), max_tokens=2000)

            # Generating image
            response = openai.Image.create(
                prompt="Photo of " + recipe.name,
                n=1,
                size="1024x1024",
            )

            tags_to_return = []

            for tag in recipe.tags.all():
                tags_to_return.append(tag.name)

            to_save['recipes'].append({
                'name': title.choices[0].text,
                'description': completion.choices[0].text,
                'image': response["data"][0]["url"],
                'tags': tags_to_return
            })

            save_json()

            print("Saved: " + title.choices[0].text)

            print(recipe.instructions)
            print(recipe.name)
        except:
            print("Not saved")

generate_recipes_from_tag('poultry')
generate_recipes_from_tag('chicken')
generate_recipes_from_tag('poultry')
generate_recipes_from_tag('chicken')
generate_recipes_from_tag('poultry')
generate_recipes_from_tag('chicken')
generate_recipes_from_tag('seafood')
generate_recipes_from_tag('beef')
generate_recipes_from_tag('pork')
generate_recipes_from_tag('salmon')
generate_recipes_from_tag('shrimp')
generate_recipes_from_tag('eggs')
generate_recipes_from_tag('fish')
generate_recipes_from_tag('onion')
generate_recipes_from_tag('tomatoes')
generate_recipes_from_tag('carrot')
generate_recipes_from_tag('mushrooms')
generate_recipes_from_tag('zucchini')
generate_recipes_from_tag('spinach')
generate_recipes_from_tag('cucumber')
generate_recipes_from_tag('green pepper')
generate_recipes_from_tag('feta cheese')
generate_recipes_from_tag('bacon')
generate_recipes_from_tag('mozzarella cheese')
generate_recipes_from_tag('cheese')
generate_recipes_from_tag('nuts')
generate_recipes_from_tag('avocado')
generate_recipes_from_tag('dark chocolate')
generate_recipes_from_tag('full-fat yogurt')