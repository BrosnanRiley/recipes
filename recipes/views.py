from django.shortcuts import render, get_object_or_404, redirect
from recipes.models import Recipe, Ingredient, RecipeStep
from recipes.forms import RecipeForm, ReviewRatingForm, IngredientForm, RecipeStepForm
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory, inlineformset_factory
from IPython import embed

# Create your views here.


def show_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        "recipe_object": recipe,
    }
    return render(request, "recipes/detail.html", context)


def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        "recipe_list": recipes
    }
    return render(request, "recipes/list.html", context)


@login_required()
def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(False)
            recipe.author = request.user
            recipe.save()
            return redirect("create_ingredients", recipe.id)
    else:
        form = RecipeForm()
    context = {
        "form": form,
    }
    return render(request, "recipes/create.html", context)


def edit_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("edit_ingredients", recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    context = {
        "recipe_object": recipe,
        "recipe_form": form
    }
    return render(request, "recipes/edit.html", context)


@login_required
def my_recipe_list(request):
    recipes = Recipe.objects.filter(author=request.user)
    context = {
        "recipe_list": recipes,
    }
    return render(request, "recipes/list.html", context)


@login_required
def submit_review(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == "POST":
        form = ReviewRatingForm(request.POST)
        if form.is_valid():
            rating = form.save(False)
            rating.recipe = recipe
            rating.user = request.user
            rating.save()
            return redirect("show_recipe", recipe.id)
    else:
        form = ReviewRatingForm()
    context = {
        "form": form,
        "recipe": recipe
    }
    return render(request, "recipes/review.html", context)


def create_ingredients(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    IngredientFormSet = modelformset_factory(Ingredient, form=IngredientForm, extra=8)
    if request.method == "POST":
        formset = IngredientFormSet(request.POST, queryset=Ingredient.objects.none())
        ingredients = formset.save(commit=False)
        for ingredient in ingredients:
            ingredient.recipe = recipe
            ingredient.save()
        return redirect("create_recipe_steps", recipe.id)
    else:
        formset = IngredientFormSet(queryset=Ingredient.objects.none())
    context = {
        "formset": formset,
    }
    return render(request, "recipes/edit_ingredients.html", context)


def create_recipe_steps(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    RecipeStepFormSet = modelformset_factory(
        RecipeStep,
        form=RecipeStepForm,
        extra=8)
    if request.method == "POST":
        formset = RecipeStepFormSet(request.POST,
                                    queryset=RecipeStep.objects.none())
        recipe_steps = formset.save(commit=False)
        for recipe_step in recipe_steps:
            recipe_step.recipe = recipe
            recipe_step.save()
        return redirect("show_recipe", recipe.id)
    else:
        formset = RecipeStepFormSet(queryset=RecipeStep.objects.none())
    context = {
        "formset": formset,
    }
    return render(request, "recipes/create_recipe_steps.html", context)


def edit_ingredients(request, id):
    IngredientFormSet = inlineformset_factory(
        Recipe,
        Ingredient,
        fields=["amount", "food_item"]
        )
    recipe = get_object_or_404(Recipe, id=id)
    formset = IngredientFormSet(instance=recipe)
    if request.method == "POST":
        formset = IngredientFormSet(request.POST, instance=recipe)
        if formset.is_valid():
            for ingredient in formset:
                ingredient.recipe = recipe
            formset.save()
            return redirect("edit_recipe_steps", recipe.id)
        else:
            print('Formset is invalid', formset.errors)
    else:
        formset = IngredientFormSet(instance=recipe)
    context = {
        "recipe": recipe,
        "formset": formset,
    }
    return render(request, "recipes/edit_ingredients.html", context)


def edit_recipe_steps(request, id):
    RecipeStepFormSet = inlineformset_factory(
        Recipe,
        RecipeStep,
        fields=["step_number", "instruction"]
        )
    recipe = get_object_or_404(Recipe, id=id)
    formset = RecipeStepFormSet(instance=recipe)
    if request.method == "POST":
        formset = RecipeStepFormSet(request.POST, instance=recipe)
        if formset.is_valid():
            for step in formset:
                step.recipe = recipe
            formset.save()
            return redirect("show_recipe", recipe.id)
        else:
            print('Formset is invalid', formset.errors)
    else:
        formset = RecipeStepFormSet(instance=recipe)
    context = {
        "recipe": recipe,
        "formset": formset,
    }
    return render(request, "recipes/edit_recipe_steps.html", context)
