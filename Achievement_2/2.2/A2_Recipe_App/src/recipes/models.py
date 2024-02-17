# models.py
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        "Recipe", on_delete=models.CASCADE, related_name="ingredients_used"
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="recipes_used",
    )

    def __str__(self):
        return f"{self.ingredient} - {self.recipe}"

class Recipe(models.Model):
    class Meta:
        ordering = ["title"]

    title = models.CharField(max_length=50)
    cooking_time = models.PositiveIntegerField(help_text="In minutes")
    description = models.TextField()
    difficulty = models.CharField(max_length=20, default="TBD")
    instructions = models.TextField()
    pic = models.ImageField(upload_to="recipes", default="no_picture.jpeg")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")  
    created_at = models.DateTimeField(auto_now_add=True) 

    def calculate_difficulty(self):
        from recipeingredients.models import RecipeIngredient

        num_ingredients = RecipeIngredient.objects.filter(recipe=self).count()

        if self.cooking_time < 10 and num_ingredients < 4:
            return "Easy"
        elif self.cooking_time < 10 and num_ingredients >= 4:
            return "Medium"
        elif self.cooking_time >= 10 and num_ingredients < 4:
            return "Intermediate"
        else:
            return "Hard"

    def save(self, *args, **kwargs):
        self.difficulty = self.calculate_difficulty()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipes:recipes_detail", kwargs={"pk": self.pk})

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)




