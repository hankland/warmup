# Create your views here.
from django.http import HttpResponse
from login.models import UsersModel
import login.models
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

def index(request):
    c = {}
    return render_to_response('client.html', c)

def login(request):
    return HttpResponse("<html><body>login</body></html>")

def add(request):
    return HttpResponse("<html><body>login</body></html>")

def reset(request):
    return HttpResponse("<html><body>login</body></html>")

def tests(request):
    return HttpResponse("<html><body>login</body></html>")



