from django.urls import path
from forumApp.posts import views


urlpatterns = [
    path('', views.index, name='home'),
    path('dashboard/', views.dashboard_view, name='dash'),
]
