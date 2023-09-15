from django.urls import path
from recipes.views import (
    recipe_list,
    show_recipe,
    create_recipe,
    edit_recipe,
    my_recipe_list,
    submit_review,
    create_ingredients,
    create_recipe_steps,
    edit_ingredients,
    edit_recipe_steps,
    )


urlpatterns = [
    path("", recipe_list, name="recipe_list"),
    path("<int:id>/", show_recipe, name="show_recipe"),
    path("create/", create_recipe, name="create_recipe"),
    path("<int:id>/edit/", edit_recipe, name="edit_recipe"),
    path("mine/", my_recipe_list, name="my_recipe_list"),
    path("<int:id>/review", submit_review, name="submit_review"),
    path("<int:id>/create_ingredients", create_ingredients,
         name="create_ingredients"),
    path("<int:id>/create_recipe_steps", create_recipe_steps,
         name="create_recipe_steps"),
    path("<int:id>/edit_ingredients/", edit_ingredients,
         name="edit_ingredients"),
    path("<int:id>/edit_steps/", edit_recipe_steps, name="edit_recipe_steps")
]
