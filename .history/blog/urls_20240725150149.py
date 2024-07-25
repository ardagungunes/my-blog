from django.urls import path
from . import views

urlpatterns = [
    path("", views.),
    path("posts"),
    path("posts/<slug:slug>")
]
