from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_cyprus),
    path('shalom/', views.say_cheese),
]