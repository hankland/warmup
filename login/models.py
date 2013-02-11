from django.db import models

# Create your models here.

class UsersModel(models.Model):
    user = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    count = models.IntegerField()

SUCCESS = 1
ERR_BAD_CREDENTIALS = -1
ERR_USER_EXISTS = -2
ERR_BAD_USERNAME = -3
ERR_BAD_PASSWORD = -4

def login(user, password):
    qs = UsersModel.objects.filter(user__exact=user).filter(password__exact=password)
    if not qs:
        return ERR_BAD_CREDENTIALS
    u = qs[0]
    u.count = u.count + 1
    u.save()
    return u.count

def add(user, password):
    if len(user) > 128 or len(user) == 0:
        return ERR_BAD_USERNAME
    if len(password) > 128:
        return ERR_BAD_PASSWORD
    qs = UsersModel.objects.filter(user__exact=user)
    if qs:
        return ERR_USER_EXISTS
    u = UsersModel(user=user, password=password, count=1)
    u.save()
    return SUCCESS

def TESTAPI_resetFixture():
    UsersModel.objects.all().delete()
    return SUCCESS

