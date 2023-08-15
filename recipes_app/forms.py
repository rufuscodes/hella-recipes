from django import forms
from .models import Recipe, RecipeIngredient, Ingredient, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description'] 
        
        
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'category', 'image']


RecipeIngredientFormSet = forms.inlineformset_factory(
    Recipe, 
    RecipeIngredient, 
    fields=('ingredient', 'quantity', 'measurement'), 
    extra=1,
    widgets={
        'ingredient': forms.Select(attrs={'class': 'form-control'}),
        'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        'measurement': forms.TextInput(attrs={'class': 'form-control'})
    }
)
