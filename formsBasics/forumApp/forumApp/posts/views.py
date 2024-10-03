from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from forumApp.posts.forms import PersonForm, PostCreateForm, PostDeleteForm
from forumApp.posts.models import Post


def index(request):
    form = PersonForm(request.POST or None)

    context = {
        "my_form": form,
    }

    return render(request, 'base.html', context=context)


def add_post(request):
    form = PostCreateForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('dash')

    context = {
        'form': form
    }

    return render(request, 'add-post.html', context=context)


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
    return render(request, 'delete-template.html', context)


def details_page(request, pk:int):
    post = Post.objects.get(pk=pk)

    context = {
        "post": post,
    }

    return render(request, 'details-post.html', context)


def dashboard_view(request):
    context = {
        "posts": Post.objects.all(),
    }

    return render(request, 'dashboard.html', context)
