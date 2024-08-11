from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("problemlist/", views.problem_list, name="problem_list"),
]