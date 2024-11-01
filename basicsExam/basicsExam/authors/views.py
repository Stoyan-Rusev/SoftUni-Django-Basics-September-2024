from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from basicsExam.authors.forms import AuthorCreateForm, AuthorEditForm
from basicsExam.authors.models import Author
from basicsExam.utils import get_author


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'authors/create-author.html'
    success_url = reverse_lazy('dash')


class AuthorDetailsView(DetailView):
    template_name = 'authors/details-author.html'

    def get_object(self, queryset=None):
        return get_author()


class AuthorEditView(UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'authors/edit-author.html'
    success_url = reverse_lazy('details-author')

    def get_object(self, queryset=None):
        return get_author()


class AuthorDeleteView(DeleteView):
    template_name = 'authors/delete-author.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_author()
