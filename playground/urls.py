from django.urls import path
from . import views

# url config
urlpatterns = [
    path('playground/hello', views.say_hello)
]

