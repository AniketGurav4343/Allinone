from django.urls import path

from . import views
urlpatterns = [
    path('Song_view', views.Song_view, name='Song_view'),
]