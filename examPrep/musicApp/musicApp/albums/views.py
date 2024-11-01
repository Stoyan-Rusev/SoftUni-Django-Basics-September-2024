from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from musicApp.albums.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from musicApp.albums.models import Album
from musicApp.utils import get_profile


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumCreateForm
    template_name = 'album/album-add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        profile = get_profile()
        form.instance.owner = profile
        return super().form_valid(form)


class AlbumEditView(UpdateView):
    model = Album
    template_name = 'album/album-edit.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    form_class = AlbumEditForm


class AlbumDetailsView(DetailView):
    pk_url_kwarg = 'id'
    model = Album
    template_name = 'album/album-details.html'


class AlbumDeleteView(DeleteView):
    model = Album
    form_class = AlbumDeleteForm
    pk_url_kwarg = 'id'
    template_name = 'album/album-delete.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

