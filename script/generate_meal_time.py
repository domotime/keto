import os
import openai

openai.organization = "org-hap0lN10kL9bXjWOfqoYjjLj"
openai.api_key = "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"
openai.Model.list()

import json

to_save = {'recipes': []}

with open('json_recipes/recipes.json', 'r') as fp:
    to_save = json.load(fp)

def save_json():
    global to_save
    with open('json_recipes/recipes_with_time.json', 'w') as fp:
        json.dump(to_save, fp)

from multiprocessing import Process
import asyncio

def background(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, **kwargs)



def what_is_m(recipe, index):

    if recipe == None:
        print("No recipe")
        return
    
    what_is = openai.Completion.create(engine="text-davinci-003", prompt=\
            ("Is this for main meal (lunch or dinner), breakfast or snack " + recipe + " (answer in english)"), max_tokens=500)

    print(what_is.choices[0].text)

    if "main meal" in what_is.choices[0].text:
        to_save['recipes'][index]['time'] = "main"
    elif "breakfast" in what_is.choices[0].text:
        to_save['recipes'][index]['time'] = "breakfast"
    elif "snack" in what_is.choices[0].text:
        to_save['recipes'][index]['time'] = "snack"
    else:
        to_save['recipes'][index]['time'] = "main"

    save_json()

import time

saved = []

with open('json_recipes/recipes_with_time.json', 'r') as fp:
    saved = json.load(fp)


for index in range(len(to_save['recipes'])):
    if "time" in saved['recipes'][index]:
        print("skipping")
        continue
    save_it = to_save['recipes'][index]['name']
    what_is_m(save_it, index)

    time.sleep(2)
    

    