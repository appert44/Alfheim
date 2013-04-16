"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test import Client
from alfheimweb.views import *


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
        
class LoginTest(TestCase):
    def test_login(self):
        c = Client()
        print('username: appert44 password: frey')
        print('status code = 200')
        response = c.post('/alfheimweb/registration/', {'username':'appert44','password':'frey'})
        self.assertEqual(response.status_code, 200)

      
