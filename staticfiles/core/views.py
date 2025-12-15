from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def project(request):
    return render(request, 'projects.html')


def resume(request):
    return render(request, 'resume.html')
