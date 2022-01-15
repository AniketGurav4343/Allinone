import imp
from multiprocessing.spawn import import_main_path
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response

from rest_framework.viewsets import ViewSet,ModelViewSet
class EmployeeSimpleViewSet(ViewSet):
    def list(self,request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)
        

    def retrieve(self, request, pk):
        try:
            data = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        serializer =EmployeeSerializer(data)
        return Response(serializer.data)
    
    def update(self, request, pk):
        emp = Employee.objects.get(pk=pk)
        serializer =EmployeeSerializer(emp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)

    def delete(self, request, pk):
        emp = Employee.objects.get(pk=pk)
        emp.delete()
        return Response({'Status:Data Deleted'})

class EmployeeModelViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


#  ****** Basic Authentication*****
# from rest_framework.authentication import BaseAuthentication
#from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly


# class EmployeeViewSet(viewsets.ModelViewSet):
#     serializer_class = EmployeeSerializer
#     queryset = Employee.objects.all()
    # authentication_class = [BaseAuthentication]
    # permission_classes = [IsAdminUser]
    # permission_classes = [AllowAny, IsAdminUser,IsAuthenticated] #IsAdminUser = is_staff:True
    
#  ****** end Basic Authentication*****

#  ****** session Authentication*****
# from rest_framework.authentication import SessionAuthentication
# from .custompermission import myPermission
# class EmployeeViewSet(viewsets.ModelViewSet):
#     serializer_class = EmployeeSerializer
#     queryset = Employee.objects.all()
#     authentication_class = [SessionAuthentication]
#     permission_classes = [myPermission]
#  ******end session Authentication*****

#  ******function base view Authentication*****
# from rest_framework.decorators import api_view,authentication_classes,permission_classes
# from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

# @api_view(['GET'])
# @authentication_classes([SessionAuthentication])
# @permission_classes([IsAuthenticated])
# def taskDetails_view(request, pk):
#     if request.method == 'GET':
#         data = Employee.objects.get(id=pk)
#         serializer = EmployeeSerializer(data)
#         return Response(serializer.data)
#  ****** end function base view Authentication*****

#  ****** Token Authentication*****
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    # authentication_class = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
#  ****** end Token Authentication*****
