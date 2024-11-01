from django import forms

from basicsExam.mixins import ReadOnlyMixin
from basicsExam.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('updated_at', 'author')


class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Put an attractive and unique title...'}),
            'content': forms.Textarea(
                attrs={'placeholder': 'Share some interesting facts about your adorable pets...'}),
        }
        help_texts = {
            'post_image_url': 'Share your funniest furry photo URL!',
        }


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(ReadOnlyMixin, PostBaseForm):
    read_only_fields = ['title', 'image_url', 'content']
