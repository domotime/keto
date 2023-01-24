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

with open('json_recipes/recipes.json', 'r') as fp:
    to_save = json.load(fp)

def save_json():
    global to_save
    with open('json_recipes/recipes.json', 'w') as fp:
        json.dump(to_save, fp)

done_recipes = []
for recipe in to_save['recipes']:
    done_recipes.append(recipe['id'])

from multiprocessing import Process
import asyncio

def background(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, **kwargs)

    return wrapped

@background
def create_recipe_json(recipe: Recipe):
    print("Creating recipe: " + recipe.name)
    try:
        if recipe.pk in done_recipes:
            print("Already saved")
            return
        title = openai.Completion.create(engine="text-davinci-003", prompt=\
            ("Traduci in italiano " + recipe.name), max_tokens=2000)
        
        completion = openai.Completion.create(engine="text-davinci-003", prompt=\
        ("Scrivi una ricetta in italiano di " + recipe.instructions), max_tokens=2000)
        # Generating image
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
        save_json()
    except:
        print("Not saved")


recipes = random_recipes("poultry")

for i in range(30):
    create_recipe_json(recipes[i])
exit()


if __name__ == '__main__':
    

    process_1 = Process(target=create_recipe_json,args=(recipes[0],))
    process_2 = Process(target=create_recipe_json,args=(recipes[1],))
    process_3 = Process(target=create_recipe_json,args=(recipes[2],))
    process_4 = Process(target=create_recipe_json,args=(recipes[3],))
    process_5 = Process(target=create_recipe_json,args=(recipes[4],))
    process_6 = Process(target=create_recipe_json,args=(recipes[5],))
    process_7 = Process(target=create_recipe_json,args=(recipes[6],))
    process_8 = Process(target=create_recipe_json,args=(recipes[7],))
    process_9 = Process(target=create_recipe_json,args=(recipes[8],))
    process_10 = Process(target=create_recipe_json, args=(recipes[9],))
    process_11 = Process(target=create_recipe_json, args=(recipes[10],))
    process_12 = Process(target=create_recipe_json, args=(recipes[11],))
    process_13 = Process(target=create_recipe_json, args=(recipes[12],))
    process_14 = Process(target=create_recipe_json, args=(recipes[13],))
    process_15 = Process(target=create_recipe_json, args=(recipes[14],))
    process_16 = Process(target=create_recipe_json, args=(recipes[15],))
    process_17 = Process(target=create_recipe_json, args=(recipes[16],))
    process_18 = Process(target=create_recipe_json, args=(recipes[17],))
    process_19 = Process(target=create_recipe_json, args=(recipes[18],))
    process_20 = Process(target=create_recipe_json, args=(recipes[19],))
    process_21 = Process(target=create_recipe_json, args=(recipes[20],))
    process_22 = Process(target=create_recipe_json, args=(recipes[21],))
    process_23 = Process(target=create_recipe_json, args=(recipes[22],))
    process_24 = Process(target=create_recipe_json, args=(recipes[23],))
    process_25 = Process(target=create_recipe_json, args=(recipes[24],))
    process_26 = Process(target=create_recipe_json, args=(recipes[25],))
    process_27 = Process(target=create_recipe_json, args=(recipes[26],))
    process_28 = Process(target=create_recipe_json, args=(recipes[27],))
    process_29 = Process(target=create_recipe_json, args=(recipes[28],))
    process_30 = Process(target=create_recipe_json, args=(recipes[29],))

    process_1.start()
    process_2.start()
    process_3.start()
    process_4.start()
    process_5.start()
    process_6.start()
    process_7.start()
    process_8.start()
    process_9.start()
    process_10.start()
    process_11.start()
    process_12.start()
    process_13.start()
    process_14.start()
    process_15.start()
    process_16.start()
    process_17.start()
    process_18.start()
    process_19.start()
    process_20.start()
    process_21.start()
    process_22.start()
    process_23.start()
    process_24.start()
    process_25.start()
    process_26.start()
    process_27.start()
    process_28.start()
    process_29.start()
    process_30.start()

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


