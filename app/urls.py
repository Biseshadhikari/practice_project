from django.urls import path
from .views import *




urlpatterns = [ 
    path('',Home),
    path('about',about_us)
]