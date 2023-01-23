from django.http import JsonResponse
from django.shortcuts import render
from recipes.models.tag import Tag
from recipes.models.recipe import Recipe
from recipes.models.ingredient import Ingredient

def all_tags(request):
    tags = Tag.objects.all()
    # convert queryset to list
    tags_list = list(tags.values())
    return JsonResponse(tags_list, safe=False)

def all_recipes(request):
    recipes = Recipe.objects.all()
    tags = request.GET.getlist('tags')
    # ingredients = request.GET.getlist('ingredients')

    print(tags)

    if tags:
        tags = Tag.objects.filter(name__in=tags)
        recipes = recipes.filter(tags__in=tags)
    
    """
    if ingredients:
        ingredients = Ingredient.objects.filter(name__in=ingredients)
        recipes = recipes.filter(ingredients__in=ingredients)
    """

    recipes_list = list(recipes.values())
    return JsonResponse(recipes_list, safe=False)
