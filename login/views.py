# Create your views here.
from django.http import HttpResponse
from login.models import UsersModel, add,login,TESTAPI_resetFixture
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
import json
from login.tests import SimpleTest

m = 'application/json'
def index(request):
    c = {}
    return render_to_response('client.html', c)

def log(request):
    d = json.loads(request.body)
    user = d['user']
    password = d['password']
    r = login(user,password)
    s = ''
    if r > 0:
        s = json.dumps({'errCode' : 1,'count' : r})
    else:
        s = json.dumps({'errCode' : r})
    return HttpResponse(s,content_type=m)

def a(request):
    d = json.loads(request.body)
    user = d['user']
    password = d['password']
    r = add(user,password)
    s = ''
    if r > 0:
        s = json.dumps({'errCode' : 1,'count' : r})
    else:
        s = json.dumps({'errCode' : r})
    return HttpResponse(s,content_type=m)

def r(request):
    r = TESTAPI_resetFixture()
    s = json.dumps({'errCode' : r})
    return HttpResponse(s,content_type=m)

def tests(request):
    numTests = 10
    numFailed = 0
    t = SimpleTest()
    output = "a"#t.test_basic_addition()

    s = json.dumps({'totalTests' : numTests,
                    'nrFailed' : numFailed,
                    'output' : output})
    return HttpResponse(s,content_type=m)



