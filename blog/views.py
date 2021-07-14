from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
import hashlib

# Create your views here.
def index(request):
    return render(request, "index.html", context={'time': datetime.datetime.now()})


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        data = request.POST
        print(data)
        print(data["user"])
        if hashlib.sha256(data["pass"]):
            # TODO: Set Auth Token
            print("Login")
            return redirect('/', context={'time': datetime.datetime.now()})
        else:
            print("nope")
            return redirect('/', context={'time': datetime.datetime.now()})
