from django.http import HttpResponse
from  django.shortcuts import render



def home(request):
    # return  HttpResponse('Hello World! welcome')
    return render(request, 'website/index.html')
def About(request):
    return  HttpResponse('Hello World! Anout Page')
def Contact(request):
    return  HttpResponse('Hello World! Contact page')
