from django.shortcuts import render, HttpResponse
from django.views.generic import ListView


from . import models


# Create your views here.
def home(request):
    recipes = models.Recipe.objects.all().prefetch_related('recipeingredient_set__ingredient')

    context= {
        'recipes': recipes,
    }
    return render(request,"recipes_app/home.html", context)

class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'recipes_app/home.html'

def about(request):
    
    return render(request,"recipes_app/about.html", {'title': 'About this app'})
