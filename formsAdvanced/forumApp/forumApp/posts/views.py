from datetime import datetime

from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect

from forumApp.posts.forms import PersonForm, PostCreateForm, PostDeleteForm, PostBaseForm, SearchForm, PostEditForm, \
    CommentFormSet
from forumApp.posts.models import Post


def index(request):
    form = PersonForm(request.POST or None)

    context = {
        "my_form": form,
    }

    return render(request, 'common/index.html', context=context)


def add_post(request):
    form = PostCreateForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('dash')

    context = {
        'form': form
    }

    return render(request, 'posts/add-post.html', context=context)


def delete_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    form = PostDeleteForm(instance=post)

    if request.method == "POST":
        post.delete()
        return redirect('dash')

    context = {
        "form": form,
        "post": post,
    }
    return render(request, 'posts/delete-post.html', context)


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


def dashboard_view(request):
    form = SearchForm(request.GET)
    posts = Post.objects.all()

    if request.method == 'GET':
        if form.is_valid():
            search_text = form.cleaned_data['query']
            posts = posts.filter(title__icontains=search_text)

    context = {
        "posts": posts,
        "form": form,
    }

    return render(request, 'posts/dashboard.html', context)


def edit_post(request, pk: int):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('dash')

    else:
        form = PostEditForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, 'posts/edit-post.html', context)


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

