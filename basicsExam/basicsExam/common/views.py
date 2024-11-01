from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from basicsExam.posts.models import Post
from basicsExam.utils import get_author


class IndexView(TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = get_author()

        return context


class DashboardView(ListView):
    model = Post
    template_name = 'common/dashboard.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = get_author()

        return context
