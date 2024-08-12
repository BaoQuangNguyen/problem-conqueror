from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
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

class NewProblemView(CreateView):
    model = Problem
    template_name = "problems/new_problem.html"
    fields = ['title', 'description']  # Adjust fields as necessary

    def form_valid(self, form):
        # You can add additional logic here if needed
        return super().form_valid(form)

class CreateAccountView(CreateView):
    form_class = UserCreationForm
    template_name = "problems/create_account.html"
    success_url = '/'  # Redirect to the index page or wherever after successful account creation

    def form_valid(self, form):
        # You can add additional logic here if needed
        return super().form_valid(form)
