import uuid
from recipes.models.recipe import Recipe

import requests

def translate_recipes(recipes, src_language, dest_language, subscription_key):
    endpoint = "https://api.cognitive.microsofttranslator.com"
    path = '/translate?api-version=3.0'
    params = '&to=' + dest_language
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': 'francecentral',
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    for recipe in recipes:
        body = [{
            'text': recipe.name
        }]
        request = requests.post(endpoint + path + params, headers=headers, json=body)
        response = request.json()

        recipe.name = response[0]['translations'][0]['text']

        body = [{
            'text': recipe.instructions
        }]
        request = requests.post(endpoint + path + params, headers=headers, json=body)
        response = request.json()
        recipe.instructions = response[0]['translations'][0]['text']

        body = [{
            'text': recipe.description
        }]
        request = requests.post(endpoint + path + params, headers=headers, json=body)
        response = request.json()
        recipe.description = response[0]['translations'][0]['text']

        print(recipe.name)

        print(recipe.instructions)

        return

    return recipes

recipes = Recipe.objects.all().order_by('name')
src_language = "en"
dest_language = "it"
subscription_key = "e5bb601154444624be5b2afefb0d2281"

translated_recipes = translate_recipes(recipes, src_language, dest_language, subscription_key)