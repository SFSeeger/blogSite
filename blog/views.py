from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Author, Blogpage
import datetime
import hashlib

# Create your views here.
def index(request):
    return render(request, "index.html", context={'time': datetime.datetime.now()})


def login(request):
    if request.method == "GET":
        return render(request, 'login.html', context={'error':False, 'error_msg':''})
    else:
        data = request.POST
        if Author.objects.all().filter(username=data['user'], password=hashlib.sha256(data["pass"].encode())):
            # TODO: Set Auth Token
            print("Login")
            return redirect('/', context={'time': datetime.datetime.now()})
        else:
            print("nope")
            return render(request, 'login.html', context={'error':True, 'error_msg':'Username or password incorrect'})

def login_register(request):
    if request.method == "GET":
        return render(request, "register.html", context={'error':False, 'error_msg':''})
    else:
        data = request.POST
