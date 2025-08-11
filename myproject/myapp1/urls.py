from django.urls import path
from .views import *
from .api import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


urlpatterns = [
    path('h/', hello_func, name='hello_func'),
    path('start/', start, name='start'),
    path('last/', last, name='last'),
    path('link/', link, name='link'),
    path('navbar/', navbar, name='navbar'),
    path('home/', home, name='home'),
    path('company/', company, name='company'),
    path('marketplace/', marketplace, name='marketplace'),
    path('contact/', contact, name='contact'),
    path('features/', features, name='features'),
    path('team/', team, name='team'),
    path('dep/',department,name="department"),
    path('Individual/',Individual_view,name="Individual"),
    path('Individuallist/',Individual_list,name="Individual_list"),
    path('edit/<int:i_id>',edit,name='edit'),
    
    path('login/',login,name='login'),
    path('logout/',login,name='logout_view'),
    path('signup/',signup,name='signup'),
]

# for api

urlpatterns=[
    path('list_dept',list_dept),
    path('post/',post_dept),
    path('ind/',Individual1.as_view()),
    path('token/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('log/',login1.as_view()),

]