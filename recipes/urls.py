from django.urls import path
from .views import all_recipes, all_tags

urlpatterns = [
    path('tags/', all_tags, name='all_tags'),
    path('recipes/', all_recipes, name='all_recipes'),
]