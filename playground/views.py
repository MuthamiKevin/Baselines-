from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound    
from django.views.decorators.http import require_http_methods  
from .models import Feature
# Create your views here.
def say_hello(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'fast'
    feature1.detail = 'Our service are very quick'
    
    
    return render(request, 'hello.html', {'Feature': feature1})