# Generated by Django 4.2.8 on 2024-01-14 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_remove_recipe_name_recipe_description_recipe_pic_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['title']},
        ),
    ]
