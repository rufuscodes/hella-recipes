from django.shortcuts import render, HttpResponse


recipes = [{
    'author': "Rufus",
    'title': 'Da Town Pizza',
    'directions': "Prep and cook",
    'date_posted': 'April 16th, 2023'
    
}]


# Create your views here.
def home(request):
    context= {
        'recipes': recipes,
    }
    return render(request,"recipes_app/home.html", context)

def about(request):
    
    return render(request,"recipes_app/about.html", {'title': 'About this app'})
