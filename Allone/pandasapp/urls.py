from django.urls import path,include
from . import views
urlpatterns = [
        path('student_pd_view', views.student_view, name='student_pd_view'),
]