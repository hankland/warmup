# Create your views here.
from django.http import HttpResponse
from login.models import UsersModel
import login.models
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
import json

m = 'application/json'
def index(request):
    c = {}
    return render_to_response('client.html', c)

def login(request):
    d = json.loads(request.body)
    user = d['user']
    password = d['password']
    r = login.models.login(user,password)
    s = ''
    if r > 1:
        s = json.dumps({'errCode' : 1,'count' : r})
    else:
        s = json.dumps({'errCode' : r})
    return HttpResponse(s,content_type=m)

def add(request):
    d = json.loads(request.body)
    user = d['user']
    password = d['password']
    r = login.models.add(user,password)
    s = ''
    if r > 1:
        s = json.dumps({'errCode' : 1,'count' : r})
    else:
        s = json.dumps({'errCode' : r})
    return HttpResponse(s,content_type=m)

def reset(request):
    return HttpResponse("<html><body>login</body></html>")

def tests(request):
    return HttpResponse("<html><body>login</body></html>")



