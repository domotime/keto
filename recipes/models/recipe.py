from django.db import models

from recipes.models.ingredient import Ingredient
from recipes.models.tag import Tag

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    minutes = models.IntegerField(default=0)
    instructions = models.TextField()
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient', null=True)
    tags = models.ManyToManyField(Tag)

    calories = models.IntegerField()
    fat = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    sugar = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    sodium = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    carbohydrate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    measurement = models.CharField(max_length=255, default='')
