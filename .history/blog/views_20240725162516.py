from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def starting_page(request):
    return render(request, "blog/index.html")

def posts(request):
    return HttpResponse("<h1>All Posts!</h1>")

def post_detail(request, slug):
    print(slug)
    print(slug)
    return HttpResponse("<h1>Single Post!</h1>")


    
