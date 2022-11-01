from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")

def url1(request):
    return render(request, "project.html")