from django.http import HttpResponse
from django.urls import path, include

from musicApp.albums.views import AlbumCreateView, AlbumDetailsView, AlbumEditView, AlbumDeleteView

urlpatterns = [
    path('add/', AlbumCreateView.as_view(), name='add-album'),
    path('<int:id>/', include([
        path('details/', AlbumDetailsView.as_view(), name='details-album'),
        path('edit/', AlbumEditView.as_view(), name='edit-album'),
        path('delete/', AlbumDeleteView.as_view(), name='delete-album'),
    ])),
]
