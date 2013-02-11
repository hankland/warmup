# Create your views here.
from django.http import HttpResponse
from login.models import UsersModel
import login.models
from django.shortcuts import render


def index(request):
    return render('client.html')

