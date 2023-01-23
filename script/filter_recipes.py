from recipes.models.recipe import Recipe

def delete_recipes_without_tag(tag_name):
    # Get all recipes that do not have the specified tag
    recipes_to_delete = Recipe.objects.filter(tags__name__iexact=tag_name)

    # Delete the recipes
    recipes_to_delete.delete()

delete_recipes_without_tag("very-low-carbs")