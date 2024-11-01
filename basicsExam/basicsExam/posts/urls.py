from django.urls import path, include

from basicsExam.posts.views import PostCreateView, PostDetailsView, PostEditView, PostDeleteView

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create-post'),
    path('<int:post_id>', include([
        path('details/', PostDetailsView.as_view(), name='details-post'),
        path('edit/', PostEditView.as_view(), name='edit-post'),
        path('delete/', PostDeleteView.as_view(), name='delete-post'),
    ]))
]
