# Create your views here.
from django.http import HttpResponse
from login.models import UsersModel
import login.models


def index(request):
    return HttpResponse("<html><body>Hello</body></html>")

