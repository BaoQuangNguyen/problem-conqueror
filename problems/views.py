from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the problems index.")

def problem_list(request):
    return HttpResponse("This is the problem list page")