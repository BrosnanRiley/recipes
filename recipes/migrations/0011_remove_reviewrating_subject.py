# Generated by Django 4.2.4 on 2023-09-07 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_alter_reviewrating_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewrating',
            name='subject',
        ),
    ]
