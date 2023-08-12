from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, related_name='recipes', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)
    favorited_by = models.ManyToManyField(User, related_name='favorited_recipes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse("recipes-detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    image_url = models.URLField(blank=True, null=True) 

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    measurement = models.CharField(max_length=50)  # grams, cups, tablespoons

    def __str__(self):
        return f"{self.quantity} {self.measurement} of {self.ingredient.name} for {self.recipe.title}"


