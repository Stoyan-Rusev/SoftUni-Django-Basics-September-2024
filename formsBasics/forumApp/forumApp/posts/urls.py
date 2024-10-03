from django.urls import path, include
from forumApp.posts import views


urlpatterns = [
    path('', views.index, name='home'),
    path('dashboard/', views.dashboard_view, name='dash'),
    path('add-post/', views.add_post, name='add-post'),
    path('<int:pk>/', include([
        path('delete-post/', views.delete_post, name='delete-post'),
        path('details-post/', views.details_page, name='details-post')
    ]))
]
