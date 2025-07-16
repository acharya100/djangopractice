from django.urls import path
from .views import *

urlpatterns = [
    path('', hello_func, name='hello_func'),
    path('start/', start, name='start'),
    path('last/', last, name='last'),
    path('link/', link, name='link'),
    path('navbar/', navbar, name='navbar'),
    path('home/', home, name='home'),
    path('company/', company, name='company'),
    path('marketplace/', marketplace, name='marketplace'),
    path('contact/', contact, name='contact'),
    path('features/', features, name='features'),
    path('team/', team, name='team')
]