from django.shortcuts import render
from django.http import HttpResponse

from .tasks import test_task
# Create your views here.

def index_view(request):
    test_task.delay(10)
    return HttpResponse("<H1>hello, celery</H1>")
