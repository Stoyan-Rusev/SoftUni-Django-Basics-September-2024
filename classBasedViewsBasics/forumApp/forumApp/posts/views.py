from datetime import datetime

from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import RedirectView, TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView

from forumApp.posts.forms import PersonForm, PostCreateForm, PostDeleteForm, PostBaseForm, SearchForm, PostEditForm, \
    CommentFormSet
from forumApp.posts.models import Post


class IndexView(TemplateView):
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
            return ['common/index_logged_in.html']
        else:
            return ['common/index.html']


# def index(request):
#     form = PersonForm(request.POST or None)
#
#     context = {
#         "my_form": form,
#     }
#
#     return render(request, 'common/index.html', context=context)


class DashboardView(ListView, FormView):
    template_name = 'posts/dashboard.html'
    context_object_name = 'posts'
    model = Post

    form_class = SearchForm
    success_url = reverse_lazy('dash')

    def get_queryset(self):
        queryset = self.model.objects.all()

        if 'query' in self.request.GET:
            query = self.request.GET.get('query')

            if query:
                queryset = queryset.filter(title__icontains=query)

        return queryset


# def dashboard_view(request):
#     form = SearchForm(request.GET)
#     posts = Post.objects.all()
#
#     if request.method == 'GET':
#         if form.is_valid():
#             search_text = form.cleaned_data['query']
#             posts = posts.filter(title__icontains=search_text)
#
#     context = {
#         "posts": posts,
#         "form": form,
#     }
#
#     return render(request, 'posts/dashboard.html', context)


class AddPostView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/add-post.html'
    success_url = reverse_lazy('dash')


# def add_post(request):
#     form = PostCreateForm(request.POST or None, request.FILES or None)
#
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect('dash')
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'posts/add-post.html', context=context)


class DeletePostView(DeleteView, FormView):
    model = Post
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('dash')
    form_class = PostDeleteForm

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post = Post.objects.get(pk=pk)
        return post.__dict__


# def delete_post(request, pk: int):
#     post = Post.objects.get(pk=pk)
#     form = PostDeleteForm(instance=post)
#
#     if request.method == "POST":
#         post.delete()
#         return redirect('dash')
#
#     context = {
#         "form": form,
#         "post": post,
#     }
#     return render(request, 'posts/delete-post.html', context)


def details_page(request, pk: int):
    post = Post.objects.get(pk=pk)
    formset = CommentFormSet(request.POST or None)

    if request.method == 'POST':
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()

            return redirect('details-post', pk=post.id)

    context = {
        "post": post,
        'formset': formset,
    }

    return render(request, 'posts/details-post.html', context)


class EditPostView(UpdateView):
    template_name = 'posts/edit-post.html'
    model = Post
    success_url = reverse_lazy('dash')

    def get_form_class(self):
        if self.request.user.is_superuser:
            return modelform_factory(Post, fields=('title', 'content', 'author', 'languages', 'image'))
        return modelform_factory(Post, fields=('content', ))


# def edit_post(request, pk: int):
#     post = Post.objects.get(pk=pk)
#
#     if request.method == 'POST':
#         form = PostEditForm(request.POST, instance=post)
#
#         if form.is_valid():
#             form.save()
#             return redirect('dash')
#
#     else:
#         form = PostEditForm(instance=post)
#
#     context = {
#         'form': form,
#         'post': post,
#     }
#
#     return render(request, 'posts/edit-post.html', context)


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

