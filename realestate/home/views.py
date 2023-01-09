from django.shortcuts import render
from django.http import HttpResponse


def say_cyprus(request):
    return render(request, 'hello.html', {'name': 'Yakov'})
