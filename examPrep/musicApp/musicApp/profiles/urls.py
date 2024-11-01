from django.http import HttpResponse
from django.urls import path

from musicApp.profiles.views import ProfileDetailsView, ProfileDeleteView

urlpatterns = [
    path('details/', ProfileDetailsView.as_view(), name='details-profile'),
    path('delete/', ProfileDeleteView.as_view(), name='delete-profile')
]
