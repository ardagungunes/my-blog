from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page),
    path("posts"),
    path("posts/<slug:slug>")
]
