from django.urls import path,include

from . import views
# from rest_frame.routers import *


from rest_framework.urlpatterns import format_suffix_patterns

# blog_list=EmployeeViewSet.as_view({'get':'list'})
# blog_detail=EmployeeViewSet.as_view({'get':'retrieve',})

# from rest_framework.routers import DefaultRouter
# from .views import EmployeeViewSet

# router = DefaultRouter()
# router.register('empoyeeviewset',views.EmployeeViewSet,basename='empoyeeviewset')


urlpatterns = [
    # path('api/',include(router.urls)),
    #******* Function base *************
    path('ApiOverView', views.ApiOverView_view, name='ApiOverView'),
    path('task-list', views.taskList_view, name='task-list'),
    path('task-details/<str:pk>/', views.taskDetails_view, name='task-details'),
    path('task-create', views.taskCreate_view, name='task-create'),
    path('task-update/<str:pk>/', views.taskUpdate_view, name='task-update'),
    path('task-delete/<str:pk>/', views.taskDelete_view, name='task-delete'),

    #******* class base *************
    path('EmployeeList/', views.EmployeeList.as_view()),
    path('Employee/<int:pk>/', views.EmployeeDetail.as_view()),

    #******* Using Mixin generic (apiView) *************
    path('EmployeeFMixinList', views.EmployeeFMixinList.as_view()),
    path('EmployeeFMixintDetail/<int:pk>/', views.EmployeeFMixinDetail.as_view()),

    path('EmployeeCombineMixinList', views.EmployeeCombineMixinList.as_view()),
    path('EmployeeCombineMixinDetail/<int:pk>/', views.EmployeeCombineMixinDetail.as_view()),

    #******* Using viewset *************
    # path('model_viewsets/', blog_list, name="blog-list"),
    # path('model_viewsets/<int:pk>/', blog_detail, name="blog-detail"),

]
urlpatterns = format_suffix_patterns(urlpatterns)