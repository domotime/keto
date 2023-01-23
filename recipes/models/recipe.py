from django.db import models

import json

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
    
    def to_json(self):
        json_recipe = {
            "id": self.id,
            "name": self.name,
            "minutes": self.minutes,
            "instructions": self.instructions,
            "description": self.description,
            "calories": float(self.calories),
            "fat": float(self.fat),
            "sugar": float(self.sugar),
            "sodium": float(self.sodium),
            "carbohydrate": float(self.carbohydrate),
            "protein": float(self.protein),
            "ingredients": [{"id": ingr.id, "name": ingr.name} for ingr in self.ingredients.all()],
            "tags": [{"id": tag.id, "name": tag.name} for tag in self.tags.all()],
        }
        return json.dumps(json_recipe, indent=4)

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    measurement = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.ingredient.name