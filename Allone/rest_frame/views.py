from django.shortcuts import get_object_or_404, render
from rest_framework import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import JsonResponse


from .serializers import *
from rest_frame.models import Employee

# Create your views here.

#********************* Function base rest API ******************
@api_view(['GET'])
def ApiOverView_view(request):
    api_urls ={
        'List' : '/task-list/',
        'Detail view' : '/task-detail/<str:pK>/',
        'Create' : '/task-create/',
        'Update' : '/task-update/<str:pK>/',
        'Delete' : '/task-delete/<str:pK>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def taskList_view(request):
    if request.method == 'GET':
        data = Employee.objects.all()
        serializer = EmployeeSerializer(data, many=True)
        #return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

@api_view(['GET'])
def taskDetails_view(request, pk):
    if request.method == 'GET':
        data = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(data)
        return Response(serializer.data)

@api_view(['POST'])
def taskCreate_view(request):
    serializer = EmployeeSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def taskUpdate_view(request,pk):
    emp = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(instance=emp, data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

    
@api_view(['DELETE'])
def taskDelete_view(request,pk):
    emp = Employee.objects.get(id=pk)
    emp.delete()
    return Response("Data delete successfull")


#********************* Class base rest API ******************
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EmployeeList(APIView):
    """
    List all Employees, or create a new Employee.
    """
    def get(self, request, format=None):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(APIView):
    """
    Retrieve, update or delete a employee instance.
    """
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#************************ Using Mixin generic (apiview) ************************
from rest_framework import mixins
from rest_framework import generics

class EmployeeFMixinList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EmployeeFMixinDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class EmployeeCombineMixinList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeCombineMixinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


    
#************************ Using viewset ************************
# from rest_framework.viewsets import ViewSet,ModelViewSet
# class EmployeeModelViewSet(ModelViewSet):
#     serializer_class = EmployeeSerializer
#     queryset = Employee.objects.all()

# class EmployeeViewSet(ViewSet):
#     def list(self,request):
#         employee = Employee.objects.all()
#         serializer = EmployeeSerializer(employee, many=True)
#         return response(serializer.data)

#     # return on blog item
#     def retrieve(self,request, pk):
#         try:
#             data = Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             return Response("status.HTTP_404_NOT_FOUND")
#         serializer =EmployeeSerializer(data)
#         return response(serializer.data)