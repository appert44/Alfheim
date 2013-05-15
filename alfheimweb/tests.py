"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test import Client
from alfheimweb.views import *
from django.contrib.auth.models import User
from django.http import HttpResponse

                     
class LoginTest(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_login(self):
        User.objects.create_user('appert44', 'appert@appert44.org', 'password')
        user = self.client.login(username='appert44', password='password')
        response = self.client.post('/alfheimweb/registration/', {'username':'appert44','password':'password'})
        print('....................1e test du login avec un mot de passe correct....................')
        print(response)
        
    def test_login_fail(self):
        User.objects.create_user('appert44', 'appert@appert44.org', 'password')
        user = self.client.login(username='appert44', password='password')
        response = self.client.post('/alfheimweb/registration/', {'username':'appert44','password':'truc'})
        print('....................2e test du login avec un mot de passe faux....................')
        print(response)

            
class get_graphtest(TestCase):
    def test_graph(self):
        c = Client()
        response= c.post ('/alfheimweb/measure/', {'time':'04/17/2013', 'sensor_type':'temp', 'value':'22.00', 'device_sn':'orvault'})
        datatest = TableBrut.objects.count()
        self.assertEqual(datatest, 1)
        result=c.get ('/alfheimweb/graph/')
        print('....................Test de la methode get_graph()....................')
        print(result)
        self.assertEqual(result.status_code, 200)        
        if result.status_code == 200:
            print('Trame de retour correcte')
        else:
            print('.........FAIL!')