from django.urls import path
from . import views

'app/modle_viewtype'
'recipes_app/recipe_detail.html'


urlpatterns = [
    path('', views.RecipeListView.as_view(), name="recipes-home"),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name="recipes-detail"),
    path('recipe/create/', views.RecipeCreateView.as_view(), name="recipes-create"),
    path('recipes/<int:pk>/update/', views.RecipeUpdateView.as_view(), name="recipes-update"),
    path('recipes/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name="recipes-delete"),
    path('search/', views.RecipeSearchView.as_view(), name="search_recipes"),
    path('about/', views.about, name="recipes-about"),
    path('ingredient/<int:pk>/', views.IngredientDetailView.as_view(), name="ingredient-detail"),
    path('recipes/<int:pk>/favorite/', views.FavoriteRecipe, name="favorite-recipe"),
    path('recipes/<int:pk>/unfavorite/', views.UnfavoriteRecipe, name="unfavorite-recipe"),
    path('favorites/', views.UserFavoriteRecipes.as_view(), name="user-favorites"),


]
