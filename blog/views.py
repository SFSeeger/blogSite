from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Author, Blogpage
# from .forms import SignUP
import datetime
import hashlib
import re

phone_verifier = r''
anonym_user = 'Anonymous User'

# Create your views here.
def index(request):
    name = Author.objects.filter(id=request.session.get('member_id')).first()
    return render(request, "index.html", context={'time': datetime.datetime.now(), 'name':name.name if name else anonym_user})


def login(request):
    if request.method == "GET":
        return render(request, 'login.html', context={'error':False, 'error_msg':''})
    else:
        data = request.POST
        author = Author.objects.all().filter(username=data['user'].lower(), password=hashlib.sha256(data["pass"].encode()).hexdigest())
        if author.exists():
            request.session['member_id'] = author[0].id
            print("Login")
            name = Author.objects.filter(id=request.session.get('member_id')).first()
            return redirect('/', context={'time': datetime.datetime.now(),
                                          'name': name.name if name else anonym_user})
        else:
            print("nope")
            return render(request, 'login.html', context={'error':True, 'error_msg':'Username or password incorrect'})


def logout(request):
    try:
        del request.session["member_id"]
    except KeyError:
        pass
    return redirect('/', context={'time':datetime.datetime.now(), 'name': anonym_user})

def login_register(request):
    if request.method == "GET":
        return render(request, "register.html", context={'error':False, 'error_msg':''})
    else:
        data = request.POST
        if Author.objects.all().filter(username=data['user'].lower()).exists():
            return render(request, "register.html", context={'error': True, 'error_msg': 'Username already exists'})
        if data["pass"] != data["pass2"]:
            return render(request, "register.html", context={'error': True, 'error_msg': 'Passwords don\'t match'})
        if data["phone"]:
            # TODO: remove .+' 'etc.
            if re.match(phone_verifier, data["phone"]):
                # TODO REGISTER with phone
                print("Phone")
            return render(request, "register.html", context={'error': True, 'error_msg':'Invalid Phone Number'})
        else:
            a = Author(name=data["name"], username=data["user"].lower(),
                       password=hashlib.sha256(data["pass"].encode()).hexdigest(),
                       email=data["email"])
            a.save()
            return redirect('/login/', context={'error': True, 'error_msg': 'Account created!'})


def blog_page(request,user, post_name):
    print(user, post_name)
    return HttpResponse(user+" "+post_name)
