import pandas as pd
from recipes.models.ingredient import Ingredient

def import_ingredients(file_path):
    df = pd.read_csv(file_path)

    for index, row in df.iterrows():
        ingredient = Ingredient()

        ingredient.name = row["Ingredient"]
        ingredient.save()

PATH = "/Users/alessandrotisi/Downloads/ingredients.csv"

import_ingredients(PATH)