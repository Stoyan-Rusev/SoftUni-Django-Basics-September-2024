from django.http import HttpResponse
from django.shortcuts import render

from djangoIntroduction.todo_app.models import Task


# Create your views here.
def my_view(request):
    return HttpResponse("<h1>Hello World</h1>")


def add_view(request):
    return HttpResponse("<h1>ADD</h1>")


def delete_view(request):
    return HttpResponse("<h1>DELETE</h1>")


def show_tasks(request):
    tasks = Task.objects.all()

    result = [
        "<h1>Tasks:</h1>",
        "<ul>",
        *[f"<li>{t.name}</li>" for t in tasks],
        "</ul>"
    ]

    return HttpResponse("\n".join(result))


def index(request):
    title_filter = request.GET.get('title_filter', '')

    tasks = Task.objects.filter(name__icontains=title_filter)

    context = {
        'title_filter': title_filter,
        'tasks': tasks,
    }

    return render(request, 'tasks/index.html', context)

