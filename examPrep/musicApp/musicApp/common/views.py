from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from musicApp.albums.models import Album
from musicApp.profiles.forms import ProfileCreateForm
from musicApp.utils import get_profile


class HomePage(ListView, BaseFormView):
    model = Album
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

    def get_template_names(self):
        profile = get_profile()

        if profile:
            return ['common/home-with-profile.html']

        return ['common/home-no-profile.html']

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)
