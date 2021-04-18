from django.shortcuts import render
from .models import News


# Create your views here.

def home(request):

    data = News.objects.all()

    return render(request, "index.html", {"posts":data})
