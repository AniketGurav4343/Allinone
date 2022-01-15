from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def Song_view(request):
    song = Song.objects.filter(song_name="hum sath sath hai")
    print(song)
    html = "<html><body>It is now </body></html>"
    return HttpResponse(html)

# python manage.py shell
# Song.objects.filter(user=5)
# Song.objects.filter(user__username__startswith="aniket")