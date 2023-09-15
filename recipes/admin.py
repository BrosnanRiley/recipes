from django.contrib import admin
from recipes.models import RecipeStep, Ingredient, Recipe, ReviewRating
# Register your models here.


@admin.register(RecipeStep)
class RecipeStepAdmin(admin.ModelAdmin):
    list_display = (
        "step_number",
        "instruction",
        "id",
    )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        "amount",
        "food_item",
        "id",
    )


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "picture",
        "description",
    )


@admin.register(ReviewRating)
class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = (
        "recipe",
        "user",
        "review",
        "score",
    )

