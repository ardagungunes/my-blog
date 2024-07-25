from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page),
    path("posts", views.),
    path("posts/<slug:slug>")
]
