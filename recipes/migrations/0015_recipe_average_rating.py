# Generated by Django 4.2.4 on 2023-09-08 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0014_rename_rating_reviewrating_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='average_rating',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
