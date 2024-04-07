from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound    
from django.views.decorators.http import require_http_methods  

# Create your views here.
def say_hello(request):
    return HttpResponse('Hello world')