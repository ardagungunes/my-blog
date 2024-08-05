from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def starting_page(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog")

def post_detail(request, slug):
    print(slug)
    print(slug)
    return HttpResponse("<h1>Single Post!</h1>")


    
