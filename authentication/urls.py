# Create your tests here.
from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login_view'),
    path('logout/', logout, name='logout'),
]