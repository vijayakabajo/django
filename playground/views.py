from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# takes a request---->returns a response

def say_hello(request):
    # can pull data from db
    # transform
    # send email
    return HttpResponse('helloo')
