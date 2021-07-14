from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    return render(request, "index.html", context={'time': datetime.datetime.now()})

def login(request):
    return render(request, 'login.html')