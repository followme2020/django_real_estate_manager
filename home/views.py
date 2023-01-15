from django.shortcuts import render
from django.http import HttpResponse


def say_cyprus(request):
    return render(request, 'hello.html', {'name': 'Yakov'})


def say_cheese(request):
    return render(request, 'shalom.html')
