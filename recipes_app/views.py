from django.shortcuts import render, HttpResponse



# Create your views here.
def home(request):
    return HttpResponse("<h1>welcome</h1>")

def home(request):
    return HttpResponse('<h1>About page</h1>')