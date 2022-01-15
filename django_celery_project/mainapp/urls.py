import imp
from django.urls import path,include
from .views import *
urlpatterns = [
    path('', index_view, name='index')
]