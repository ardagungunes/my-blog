from datetime import date

from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Post, Tag

all_posts = [
    
]

def get_date(post):
    return post['date']

def get_single_post(slug):
    for post in all_posts:
        if slug == post["slug"]:
            return post
        
    

# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    print(latest_posts)
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html",{
        "all_posts": Post.objects.all()
    })

def post_detail(request, slug):
    return render(request, "blog/post-detail.html",{
        "single_post": Post.objects.
    })


    
