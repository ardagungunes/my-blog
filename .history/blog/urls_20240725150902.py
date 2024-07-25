from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts),
    path("posts/<slug:slug>", views.post_detail)
]
