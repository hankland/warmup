"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from login.models import UsersModel, add,login,TESTAPI_resetFixture

class Test(TestCase):
    def simple_add(self):
        TESTAPI_resetFixture()
        r = add('name','pass')
        self.assertTrue(r==1)
    def simple_reset(self):
        TESTAPI_resetFixture()
        r = add('name','pass')
        self.assertTrue(r==1)
        r = TESTAPI_resetFixture()
        self.assertTrue(r==1)
        r = add('name','pass')
        self.assertTrue(r==1)
    def short_username(self):
        TESTAPI_resetFixture()
        r = add('','pass')
        self.assertTrue(r==-3)
    def long_username(self):
        TESTAPI_resetFixture()
        name = """aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""
        r = add(name,'pass')
        self.assertTrue(r==-3)
    def long_pass(self):
        TESTAPI_resetFixture()
        password = """aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""
        r = add('name',password)
        self.assertTrue(r==-4)
    def existing_user(self):
        TESTAPI_resetFixture()
        r = add('name','pass')
        self.assertTrue(r==1)
        r = add('name','pass')
        self.assertTrue(r==-2)
    def simple_login(self):
        TESTAPI_resetFixture()
        r = add('name','pass')
        self.assertTrue(r==1)
        r = login('name','pass')
        self.assertTrue(r==2)
    def wrong_pass(self):
        TESTAPI_resetFixture()
        r = add('name','pass')
        self.assertTrue(r==1)
        r = login('name','wrong')
        self.assertTrue(r==-1)
    def wrong_user(self):
        TESTAPI_resetFixture()
        r = add('name','pass')
        self.assertTrue(r==1)
        r = login('wrong','pass')
        self.assertTrue(r==-1)
    def two_users(self):
        TESTAPI_resetFixture()
        r = add('name1','pass1')
        self.assertTrue(r==1)
        r = add('name2','pass2')
        self.assertTrue(r==1)
        r = login('name1', 'pass1')
        self.assertTrue(r==2)
        r = login('name1', 'pass1')
        self.assertTrue(r==3)
        r = login('name2', 'pass2')
        self.assertTrue(r==2)
        
        


