from django.urls import path
from . import views


urlpattern = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>",views.post_detail, name="post_detail-page")
]