import imp
from multiprocessing import context
from django.shortcuts import render
from pandasapp.models import student
import pandas as pd
# Create your views here.
def student_view(request):
    item= student.objects.all().values()
    df = pd.DataFrame(item)
    data_dict={
        'df':df.to_html()
    }
    return render(request, 'pandas_data.html',context=data_dict)
