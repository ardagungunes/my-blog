from datetime import date

from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Arda",
        "date": date(2024,7,26),
        "title": "Mountain Hiking",
        "excerpt": ""
    }
]

# Create your views here.

def starting_page(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail.html")


    
