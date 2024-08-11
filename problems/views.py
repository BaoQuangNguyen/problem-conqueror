from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from .models import Problem, SubProblem


class IndexView(TemplateView):
    template_name = "problems/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['problems'] = Problem.objects.all()
        return context
    

class ProblemListView(ListView):
    model = Problem
    template_name = "problems/problem_list.html"
    context_object_name = "problems"


class ProblemDetailView(DetailView):
    model = Problem
    template_name = "problems/problem_detail.html"
    context_object_name = "problem"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sub_problems"] = SubProblem.objects.filter(problem=self.object)
        return context