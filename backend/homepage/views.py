from django.shortcuts import render

# from django.http import HttpResponse




def HeroSection(request):
    return render(request, 'homepage/index.html')
# def About(request):
#     return  HttpResponse('Hello World! Anout Page')
# def Contact(request):
#     return  HttpResponse('Hello World! Contact page')
