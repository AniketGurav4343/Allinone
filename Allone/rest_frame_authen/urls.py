from gettext import install
from posixpath import basename
from django.urls import path,include
from django.contrib import admin
from . import views
from rest_frame_authen.views import EmployeeViewSet,EmployeeSimpleViewSet,EmployeeModelViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('employeeapi',views.EmployeeViewSet,basename='employeeapi')
router.register('EmployeeSimple',views.EmployeeSimpleViewSet,basename='EmployeeSimple')
router.register('EmployeeModel',views.EmployeeModelViewSet,basename='EmployeeModel')



#token creation using command line
# from rest_framework.authtoken import views

#token creation using API end point
from .auth import *
urlpatterns = [
    path('api/',include(router.urls)),
    #token creation using API end point
    path('gettoken/', CustomAuthToken.as_view())

    #token creation using command line
    #path('gettoken/', views.obtain_auth_token)
]

#token creation using command line
# INSTALLED_APPS = [
#     ...
#     'rest_framework.authtoken',
# ]

# pip install httpie
#http POST http://127.0.0.1:8000/gettoken/ username="aniket" password="aniket"
# {
#     "token": "a64efab31da94183c1e0ad9ef7cf505f8141417a"
# }


#token creation using API end point
# {
#     "email": "rahul@gmail.com",
#     "token": "45c91af82db89fbfecc9c2162ee14fc065edb5c8",
#     "user_id": 4
# }


#http GET http://127.0.0.1:8000/api/employeeapi/ 'Authorization:Token a64efab31da94183c1e0ad9ef7cf505f8141417a'
#http -f POST http://127.0.0.1:8000/api/employeeapi/ name=Jay salary=30000 'Authorization:Token a64efab31da94183c1e0ad9ef7cf505f8141417a'