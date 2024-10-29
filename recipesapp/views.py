from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {"name": "John"}
    return render(request, "recipesapp/index.html", context)


def about(request):
    return HttpResponse("About us")
