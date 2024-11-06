from datetime import datetime

from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import RedirectView, TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView, \
    DetailView

from forumApp.posts.forms import PostCreateForm, PostDeleteForm, PostBaseForm, SearchForm, CommentFormSet
from forumApp.posts.mixins import RestrictedTimeMixin
from forumApp.posts.models import Post


class IndexView(RestrictedTimeMixin, TemplateView):
    template_name = 'common/index.html'  # static way (will be ignored in this case because of 'get_template_names')
    extra_context = {
        'static_time': datetime.now(),
    }  # static way

    def get_context_data(self, **kwargs):  # dynamic way
        context = super().get_context_data(**kwargs)

        context['dynamic_time'] = datetime.now()

        return context

    def get_template_names(self):  # dynamic way
        if self.request.user.is_authenticated:
            return ['common/index-logged-in.html']
        else:
            return ['common/index.html']


class DashboardView(ListView, FormView):
    template_name = 'posts/dashboard.html'
    context_object_name = 'posts'
    model = Post
    paginate_by = 3
    form_class = SearchForm
    success_url = reverse_lazy('dash')

    def get_queryset(self):
        queryset = self.model.objects.all()

        if 'query' in self.request.GET:
            query = self.request.GET.get('query')

            if query:
                queryset = queryset.filter(title__icontains=query)

        return queryset


class AddPostView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/add-post.html'
    success_url = reverse_lazy('dash')


class DeletePostView(DeleteView, FormView):
    model = Post
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('dash')
    form_class = PostDeleteForm

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post = Post.objects.get(pk=pk)
        return post.__dict__


class DetailPostView(DetailView):
    model = Post
    template_name = 'posts/details-post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = CommentFormSet()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        formset = CommentFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()

            return redirect('details-post', pk=post.id)

        contex = self.get_context_data()
        contex['formset'] = formset
        return self.render_to_response(contex)


class EditPostView(UpdateView):
    template_name = 'posts/edit-post.html'
    model = Post
    success_url = reverse_lazy('dash')

    def get_form_class(self):
        if self.request.user.is_superuser:
            return modelform_factory(Post, fields=('title', 'content', 'author', 'languages', 'image'))
        return modelform_factory(Post, fields=('content', ))


def test(request):
    form = PostBaseForm(request.POST or None)
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    form_factory = modelform_factory(
        model=Post,
        fields=('title', 'author'),
    )

    if request.method == 'POST':
        redirect('test')

    context = {
        'test_form': form,
        'num_list': num_list,
        'factory': form_factory
    }

    return render(request, 'extra/test.html', context)


class RedirectHomeView(RedirectView):
    url = reverse_lazy('home')  # static way

    # def get_redirect_url(self, *args, **kwargs):  # dynamic way
    #     pass
