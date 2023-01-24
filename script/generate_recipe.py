import os
import openai

openai.organization = "org-hap0lN10kL9bXjWOfqoYjjLj"
openai.api_key = "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"
openai.Model.list()

from recipes.models.tag import Tag
from recipes.models.recipe import Recipe

from django.shortcuts import render
from random import sample
from recipes.models.recipe import Recipe
from recipes.models.tag import Tag

import json

to_save = {'recipes': []}

with open('json_recipes/recipes.json', 'r') as fp:
    to_save = json.load(fp)

def save_json():
    global to_save
    with open('json_recipes/recipes.json', 'w') as fp:
        json.dump(to_save, fp)

done_recipes = []
for recipe in to_save['recipes']:
    done_recipes.append(recipe['id'])

def random_recipes(tag_name):
    try:
        global done_recipes
        tag = Tag.objects.get(name=tag_name)
        recipes = Recipe.objects.filter(tags=tag).exclude(pk__in=done_recipes).order_by('?')[:30]
        return recipes
        if recipes.count() >= 30:
            return sample(recipes, 30)
        else:
            return recipes
    except:
        print("Error in recipe: " + tag_name)

from multiprocessing import Process
import asyncio

def background(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, **kwargs)

    return wrapped

import requests

def save_image(image_url, image_name):
    
    img_data = requests.get(image_url).content
    with open('json_recipes/images/' + image_name + '.jpg', 'wb') as handler:
        handler.write(img_data)

@background
def create_recipe_json(recipe: Recipe):
    print("Creating recipe: " + recipe.name)
    try:
        if recipe.pk in done_recipes:
            print("Already saved")
            return
        title = openai.Completion.create(engine="text-davinci-003", prompt=\
            ("Traduci in italiano " + recipe.name), max_tokens=500)

        ingredients = ""
        for ingredient in recipe.ingredients.all():
            ingredients = ingredients + ingredient.name + " "
        
        completion = openai.Completion.create(engine="text-davinci-003", prompt=\
        ("Scrivi una ricetta in italiano di " + recipe.instructions + " con prima una lista degli ingredienti"), max_tokens=3000)
        # Generating image
        try:
            response = openai.Image.create(
                prompt="tasty dish " + recipe.name + " for a recipe book without cutlery in the image", 
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
                'tags': tags_to_return,
                'id': recipe.pk
            })
            save_image(response["data"][0]["url"], str(recipe.pk))
        except:
            tags_to_return = []
            for tag in recipe.tags.all():
                tags_to_return.append(tag.name)
            to_save['recipes'].append({
                'name': title.choices[0].text,
                'description': completion.choices[0].text,
                'image': "",               
                'tags': tags_to_return,
                'id': recipe.pk
            })
        save_json()
    except Exception as e: 
        print(e)
        print("Not saved")


# recipes = random_recipes("poultry") | random_recipes("chicken") | random_recipes("seafood") | random_recipes("beef") | random_recipes("pork") | random_recipes("salmon") | random_recipes("shrimp") | random_recipes("eggs") | random_recipes("fish") | random_recipes("onions") | random_recipes("tomatoes") | random_recipes("carrots") | random_recipes("mushrooms") | random_recipes("zucchini") | random_recipes("spinach") | random_recipes("bacon") | random_recipes("cheese") | random_recipes("potatoes") | random_recipes("nuts") | random_recipes("avocado")

recipes = random_recipes("eggs")

import time

for index in range(3):
    for i in range(10):
        create_recipe_json(recipes[i])

    time.sleep(60)
exit()


if __name__ == '__main__':

    """
    generate_recipes_from_tag('poultry')
    exit()
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
    """


