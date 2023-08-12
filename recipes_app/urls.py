from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeListView.as_view(), name="recipes-home"),
    path('about/', views.about, name="recipes-about"),

]
