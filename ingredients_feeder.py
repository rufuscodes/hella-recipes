import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from recipes_app.models import Ingredient

def seed_ingredients(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            ingredient_name = line.strip()
            if ingredient_name:
                Ingredient.objects.get_or_create(name=ingredient_name) 

if __name__ == "__main__":
    seed_ingredients('ingredients.txt')
