from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def starting_page(request):
    return HttpResponse("<h1></h1>")

def posts(request):
    pass

def post_detail(request):
    pass


    
