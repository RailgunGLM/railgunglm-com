from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("index.html", views.index, name="index"),
    path("bio.html", views.bio, name="bio"),
    path("blog.html", views.blog, name="blog"),
    path("project.html", views.project, name="project"),
    path("project/dseictool.html", views.dseictool, name="dseictool"),
]