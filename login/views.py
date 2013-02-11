# Create your views here.
from django.http import HttpResponse
from login.models import UsersModel
import login.models
from django.shortcuts import render_to_response


def index(request):
    return render_to_response('client.html', {})

def login(request):
    return HttpResponse("<html><body>login</body></html>")

def add(request):
    return HttpResponse("<html><body>login</body></html>")

def reset(request):
    return HttpResponse("<html><body>login</body></html>")

def tests(request):
    return HttpResponse("<html><body>login</body></html>")



