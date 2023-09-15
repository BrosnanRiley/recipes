from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import ReviewRating


@receiver(post_save, sender=ReviewRating)
@receiver(post_delete, sender=ReviewRating)
def update_recipe_average_rating(sender, instance, **kwargs):
    recipe = instance.recipe
    ratings = ReviewRating.objects.filter(recipe=recipe)
    total_ratings = ratings.count()
    total_rating_value = sum(rating.score for rating in ratings)

    if total_ratings > 0:
        average_rating = total_rating_value / total_ratings
    else:
        average_rating = 0

    recipe.average_rating = average_rating
    recipe.save()
