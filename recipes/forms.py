from django.forms import ModelForm
from recipes.models import Recipe, ReviewRating, Ingredient, RecipeStep


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "picture",
            "description",
            ]


class ReviewRatingForm(ModelForm):
    class Meta:
        model = ReviewRating
        fields = [
            "review",
            "score",
        ]


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            "amount",
            "food_item",
        ]


class RecipeStepForm(ModelForm):
    class Meta:
        model = RecipeStep
        fields = [
            "step_number",
            "instruction",
        ]
