# Create your tasks here

from mainapp.models import Widget

from celery import shared_task

@shared_task(bind=True)
def test_task(self):
    for i in range(10):
        print(i)
    return "Done"

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_widgets():
    return Widget.objects.count()


@shared_task
def rename_widget(widget_id, name):
    w = Widget.objects.get(id=widget_id)
    w.name = name
    w.save()


#from mainapp.tasks import add
#add(2,3)