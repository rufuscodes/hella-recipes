from django.shortcuts import render, HttpResponse
from . import models


# Create your views here.
def home(request):
    recipes = models.Recipe.objects.all().prefetch_related('recipeingredient_set__ingredient')

    context= {
        'recipes': recipes,
        'test_variable': 'Hello, World!'

    }
    return render(request,"recipes_app/home.html", context)

def about(request):
    
    return render(request,"recipes_app/about.html", {'title': 'About this app'})
