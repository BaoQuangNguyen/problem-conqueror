from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("problemslist/", views.ProblemListView.as_view(), name="problem_list"),
    path("problemslist/<int:pk>/", views.ProblemDetailView.as_view(), name="problem_detail"),
]