from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "Home"),
    path("about/", views.about, name = "About"),
    path("category/", views.category, name = "Categories"),
    path("saved/", views.saved, name = "Saved"),
    path("save/<int:cid>", views.save, name = "Save"),
    path("category_languages/<str:category>", views.load_more, name = "Load_More"),
    path("read_more_language/<int:cid>", views.read_more, name = "Read_More"),
    path("search/", views.search, name = "Search")
]