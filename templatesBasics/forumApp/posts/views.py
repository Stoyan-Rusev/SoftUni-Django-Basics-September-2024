from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    context = {
        "some_text": "Hello",
        "current_time": datetime.now(),
        "person": {
            "name": "Ivan",
            "age": 18,
            "gender": "Male",
        },
        "some_list": [1, 2, 3],
        "users": ["Pesho", "Gosho", "Maria", "Miglena", "Stoyan"]
    }

    return render(request, 'base.html', context=context)


def dashboard_view(request):
    context = {
        "posts": [
            {
                "title": "How to create django project",
                "author": "Stoyan Rusev",
                "content": "Django Project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create django project (part two)",
                "author": "",
                "content": "Django Project Two",
                "created_at": datetime.now(),
            },
            {
                "title": "Rules for creating Django project",
                "author": "Ivan Rusev",
                "content": "",
                "created_at": datetime.now(),
            },
        ]
    }

    return render(request, 'dashboard.html', context)