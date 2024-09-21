from django.urls import path
from urlsAndViews.departments import views

# department app's urls
urlpatterns = [
    path('', views.index, name='home'),
    path('redirect-to-view/', views.redirect_to_view),
    path('softuni/', views.redirect_to_softuni),
    path('<int:pk>/', views.get_powered_pk),
    path('<int:pk>/<slug>/', views.get_department_from_slug_and_id),
    path('<slug:slug>/', views.get_department_from_slug),
    path('<variable>/', views.get_view_by_param),  # matches till slash
    path('<path:variable>/', views.get_view_by_param),  # matches all (with slashes)
]
