from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from urlsAndViews.departments.models import Department


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")


def get_view_by_param(request, variable):  # 'variable' should be named the same way as in urls.
    return HttpResponse(f"<h1>Your variable: {variable} </h1>")


def get_keywords(request, **kwargs):  # we get keyword (key is like we named it in urls).
    return HttpResponse(f"<h1>Your keyword: {kwargs} </h1>")


def get_powered_pk(request, pk):  # 'pk' should be named the same way as in urls.
    return HttpResponse(f"<h1>Your powered pk({pk}) is {pk**pk} </h1>")


def get_department_from_slug(request, slug):
    department = Department.objects.filter(slug=slug).first()
    if department:
        return HttpResponse(f"<h1>Department: {department.name}, Department's slug: {department.slug} </h1>")
    raise Http404("Department doesn't exist")


def get_department_from_slug_and_id(request, pk, slug):
    department = Department.objects.filter(id=pk, slug=slug).first()
    if department:
        return HttpResponse(f"<h1>Id: {department.pk}, Slug: {department.slug} </h1>")
    return HttpResponse(f"<h1>No such department</h1>")


def redirect_to_softuni(request):
    return redirect('https://www.softuni.bg/')


def redirect_to_view(request):
    return redirect('home')

