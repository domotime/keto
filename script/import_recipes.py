from ast import literal_eval
import pandas as pd
import numpy as np

from recipes.models.ingredient import Ingredient
from recipes.models.tag import Tag
from recipes.models.recipe import Recipe, RecipeIngredient

def append_unique_values(df, column_name):
    column = df[column_name].apply(literal_eval).values
    target_array = np.unique(np.concatenate(column))

    return target_array

def array_to_string(row, column_name):
    column = row[column_name].apply(literal_eval).values
    target_array = np.unique(np.concatenate(column).ravel())

    return ' '.join(row)

def import_tags(file_path):
    df = pd.read_csv(file_path)

    df['tags'] = df['tags'].apply(literal_eval)

    df['nutrition'] = df['nutrition'].apply(literal_eval)
    df['steps'] = df['steps'].apply(literal_eval)
    df['ingredients'] = df['ingredients'].apply(literal_eval)

    print(df.head())

    for index, row in df.iterrows():
        try:
            if "very-low-carbs" in row['tags']:
                recipe = Recipe()

                recipe.name = row['name']
                recipe.minutes = row['minutes']

                nutrition = row['nutrition']
                recipe.calories = nutrition[0]
                recipe.fat = nutrition[1]
                recipe.sugar = nutrition[2]
                recipe.sodium = nutrition[3]
                recipe.carbohydrate = nutrition[4]
                recipe.protein = nutrition[5]

                recipe.description = ' '.join(row['description'])
                recipe.instructions = ' '.join(row['steps'])

                recipe.save()

                for ingredient_string in row['ingredients']:
                    ingredient_obj, created = Ingredient.objects.get_or_create(name=ingredient_string)
                    recipe.ingredients.add(ingredient_obj)

                tags_strings = row['tags']
                for tag_string in tags_strings:
                    tag, created = Tag.objects.get_or_create(name=tag_string)
                    if created:
                        tag.save()
                    recipe.tags.add(tag)

                print(str(index) + "/" + str(len(df)) + "       ", end='\r')
        except:
            print("Skipping")

TAG = "/Users/alessandrotisi/Downloads/RAW_recipes.csv"

import_tags(TAG)




"""
from ast import literal_eval
import pandas as pd
import numpy as np

from recipes.models.ingredient import Ingredient
from recipes.models.tag import Tag
from recipes.models.recipe import Recipe, RecipeIngredient

def append_unique_values(df, column_name):
    column = df[column_name].apply(literal_eval).values
    target_array = np.unique(np.concatenate(column))

    return target_array

def array_to_string(row, column_name):
    column = row[column_name].apply(literal_eval).values
    target_array = np.unique(np.concatenate(column).ravel())

    return ' '.join(row)

def import_tags(file_path):
    df = pd.read_csv(file_path)

    df['tags'] = df['tags'].apply(literal_eval)
    df['nutrition'] = df['nutrition'].apply(literal_eval)
    df['steps'] = df['steps'].apply(literal_eval)
    df['ingredients'] = df['ingredients'].apply(literal_eval)

    for index, row in df.iterrows():
        recipe = Recipe()

        recipe.name = row['name']
        recipe.minutes = row['minutes']

        nutrition = row['nutrition']
        recipe.calories = nutrition[0]
        recipe.fat = nutrition[1]
        recipe.sugar = nutrition[2]
        recipe.sodium = nutrition[3]
        recipe.carbohydrate = nutrition[4]
        recipe.protein = nutrition[5]

        recipe.description = ' '.join(df['description'])
        recipe.instructions = ' '.join(df['steps'])

        recipe.save()

        for ingredient in row['ingredients']:
            ingredient_obj, created = Ingredient.objects.get_or_create(name=ingredient)
            recipe.ingredients.add(ingredient_obj)
        for tag in row['tags']:
            tag_obj, created = Tag.objects.get_or_create(name=tag)
            recipe.tags.add(tag_obj)

        print(str(index) + "/" + str(len(df)) + "       ", end='\r')

TAG = "/Users/alessandrotisi/Downloads/RAW_recipes.csv"

import_tags(TAG)
"""