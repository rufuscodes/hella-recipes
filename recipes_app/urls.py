from django.urls import path
from . import views

'app/modle_viewtype'
'recipes_app/recipe_detail.html'

urlpatterns = [
    path('', views.RecipeListView.as_view(), name="recipes-home"),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name="recipes-detail"),
    path('recipe/create/', views.RecipeCreateView.as_view(), name="recipes-create"),

    path('about/', views.about, name="recipes-about"),

]
