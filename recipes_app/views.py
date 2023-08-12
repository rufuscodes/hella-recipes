from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import RecipeForm, RecipeIngredientFormSet

from django.urls import reverse_lazy

from . import models


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        formset = RecipeIngredientFormSet(request.POST, prefix='ingredients')
        if form.is_valid() and formset.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            
            for ingredient_form in formset:
                # Set the recipe before saving the ingredient
                ingredient_instance = ingredient_form.save(commit=False)
                ingredient_instance.recipe = recipe
                ingredient_instance.save()
                
            return redirect('recipes-home')
    else:
        form = RecipeForm()
        formset = RecipeIngredientFormSet(prefix='ingredients')
    return render(request, 'your_template_name.html', {'form': form, 'formset': formset})


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
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = models.Recipe


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    template_name = 'recipes_app/recipe_form.html'
    form_class = RecipeForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = RecipeIngredientFormSet(self.request.POST, prefix='ingredients')
        else:
            context['formset'] = RecipeIngredientFormSet(prefix='ingredients')
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        form.instance.author = self.request.user

        if formset.is_valid():
            response = super().form_valid(form)
            
            formset.instance = self.object
            formset.save()
            
            return response
        else:
            return self.form_invalid(form)



class RecipeUpdateView( LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = ['title', 'description']
    
    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeDeleteView( LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recipes-home')
    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

def about(request):
    
    return render(request,"recipes_app/about.html", {'title': 'About this app'})
