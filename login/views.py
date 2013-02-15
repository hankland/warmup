# Create your views here.
from django.http import HttpResponse
from login.models import UsersModel, add,login,TESTAPI_resetFixture
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
import json
import login.models
from login.tests import Test
from unittest import TestResult

m = 'application/json'

def login(request):
    d = json.loads(request.body)
    user = d['user']
    password = d['password']
    r = models.login(user,password)
    s = ''
    if r > 0:
        s = json.dumps({'errCode' : 1,'count' : r})
    else:
        s = json.dumps({'errCode' : r})
    return HttpResponse(s,content_type=m)

def add(request):
    d = json.loads(request.body)
    user = d['user']
    password = d['password']
    r = models.add(user,password)
    s = ''
    if r > 0:
        s = json.dumps({'errCode' : 1,'count' : r})
    else:
        s = json.dumps({'errCode' : r})
    return HttpResponse(s,content_type=m)

def reset(request):
    r = models.TESTAPI_resetFixture()
    s = json.dumps({'errCode' : r})
    return HttpResponse(s,content_type=m)

def tests(request):
    test_list = ['simple_add', 'simple_reset', 
                 'short_username', 'long_username', 
                 'long_pass', 'existing_user', 
                 'simple_login', 'wrong_pass', 
                 'wrong_user', 'two_users']
    result = TestResult()
    for test in test_list:
        t = Test(test)
        t.run(result)
    
    numTests = result.testsRun
    numFailed = len(result.failures)
    output = 'ALL PASSED'
    if numFailed > 0:
        output = str(result.failures)

    s = json.dumps({'totalTests' : numTests,
                    'nrFailed' : numFailed,
                    'output' : output})
    return HttpResponse(s,content_type=m)



