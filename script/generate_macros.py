import pandas as pd
import json

df = pd.read_csv('json_recipes/recipes_with_time.csv')

from recipes.models.recipe import Recipe

# Add calories column
df['calories'] = 0

for index, row in df.iterrows():
    try:
        # Insert in df Recipe.calories

        recipe = Recipe.objects.get(name=row['name'])
        row['calories'] = recipe.calories
    except:
        continue

# Save in new csv
df.to_csv('json_recipes/recipes_with_time_and_calories.csv', index=False)