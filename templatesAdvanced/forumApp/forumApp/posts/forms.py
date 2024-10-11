from django import forms

from forumApp.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search...'
            }
        )
    )

# ------------------------------------------------------------


class PersonForm(forms.Form):
    STATUS_CHOICES = (
        (1, 'Active'),
        (2, 'Inactive'),
    )

    person_name = forms.CharField(
        max_length=10
    )
    age = forms.IntegerField()
    status = forms.IntegerField(
        widget=forms.Select(choices=STATUS_CHOICES),
    )
