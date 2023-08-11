from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="recipes-home"),
    path('about/', views.home, name="recipes-about"),

]
