from recipes.models.recipe import RecipeIngredient
from recipes.models.tag import Tag
from django.db.models import Count

def most_frequent_ingredients():
    # Get the most 20 frequent ingredients
    ingredients = RecipeIngredient.objects.values('ingredient__name').annotate(total=Count('ingredient__name')).order_by('-total')[:200]

    # Print the ingredients
    for ingredient in ingredients:
        print(ingredient['ingredient__name'])

def print_top_tags():
    top_tags = Tag.objects.annotate(num_recipes=Count('recipe')).order_by('-num_recipes')
    for tag in top_tags:
        #print(f"{tag.name}: {tag.num_recipes} recipes")
        print(tag.name)

most_frequent_ingredients()