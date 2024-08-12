from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("problemslist/", views.ProblemListView.as_view(), name="problem_list"),
    path("problemslist/<int:pk>/", views.ProblemDetailView.as_view(), name="problem_detail"),
    path("newproblem/", views.NewProblemView.as_view(), name="new_problem"),
    path("createaccount/", views.CreateAccountView.as_view(), name="create_account"),
]
