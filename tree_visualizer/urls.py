from django.urls import path
from . import views

urlpatterns = [
    path("build-tree/", views.build_tree, name="build_tree"),
    path("get-tree/", views.get_tree, name="get_tree"),
    path("traverse/", views.traverse_tree, name="traverse"),
]
