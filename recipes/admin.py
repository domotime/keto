from django.contrib import admin
from .models.ingredient import Ingredient
from .models.tag import Tag
from .models.recipe import Recipe, RecipeIngredient

admin.site.register(Ingredient)
admin.site.register(Tag)
admin.site.register(RecipeIngredient)
admin.site.register(Recipe)