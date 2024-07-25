from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def starting_page(request):
    return HttpResponse("<h1>Starting Page!</h1>")

def posts(request):
    return HttpResponse("<h1>All Posts!</h1>")

def post_detail(request):
    return HttpResponse("<h1>Single Post!</h1>")


    
