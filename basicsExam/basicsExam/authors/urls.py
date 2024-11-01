from django.urls import path

from basicsExam.authors.views import AuthorCreateView, AuthorDetailsView, AuthorEditView, AuthorDeleteView

urlpatterns = [
    path('create/', AuthorCreateView.as_view(), name='create-author'),
    path('details/', AuthorDetailsView.as_view(), name='details-author'),
    path('edit/', AuthorEditView.as_view(), name='edit-author'),
    path('delete/', AuthorDeleteView.as_view(), name='delete-author'),

]
