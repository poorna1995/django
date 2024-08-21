
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.HeroSection, name='Hero_section'),
    

]
