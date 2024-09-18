from django.urls import path
from djangoIntroduction.todo_app.views import my_view, add_view, delete_view, index, show_tasks

urlpatterns = [
    path('', index),
    path('tasks/', show_tasks),
    path('my/', my_view),
    path('add/', add_view),
    path('delete/', delete_view),
]
