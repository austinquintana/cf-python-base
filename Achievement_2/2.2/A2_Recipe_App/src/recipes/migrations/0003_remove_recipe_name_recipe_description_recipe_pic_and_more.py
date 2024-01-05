# Generated by Django 4.2.8 on 2023-12-29 07:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeingredients', '0001_initial'),
        ('ingredients', '0001_initial'),
        ('recipes', '0002_remove_recipe_description_recipe_difficulty_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='name',
        ),
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(default=datetime.datetime(2023, 12, 29, 7, 49, 25, 42537, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='pic',
            field=models.ImageField(default='no_picture.jpeg', upload_to='recipes'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='title',
            field=models.CharField(default=datetime.datetime(2023, 12, 29, 7, 49, 57, 825028, tzinfo=datetime.timezone.utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveIntegerField(help_text='In minutes'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(default='TBD', max_length=20),
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='recipeingredients.RecipeIngredient', to='ingredients.ingredient'),
        ),
    ]