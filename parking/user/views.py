from django.shortcuts import render
from django.http import HttpResponse
from django import template

class User:
    def index(request):
        return HttpResponse(render(request, "user.html", {"name": "Athar"}))