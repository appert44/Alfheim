"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test import Client
from alfheimweb.views import *

class DataBaseTest(TestCase):
    def test_database(self):
        datatest = TableBrut.objects.count()
        print('TableBrut')
        self.assertEqual(datatest, 0)
        if datatest == 0:
            print('.........OK!')
        else:
            print('.........FAIL!')
            
        H_datatest = H_agregation.objects.count()
        print('H_agregation')
        self.assertEqual(H_datatest, 0)
        if H_datatest == 0:
            print('.........OK!')
        else:
            print('.........FAIL!')

        D_datatest = D_agregation.objects.count()
        print('D_agregation')
        self.assertEqual(D_datatest, 0)
        if D_datatest == 0:
            print('.........OK!')
        else:
            print('.........FAIL!')
        M_datatest = M_agregation.objects.count()
        print('M_agregation')
        self.assertEqual(M_datatest, 0)
        if M_datatest == 0:
            print('.........OK!')
        else:
            print('.........FAIL!')

        Y_datatest = Y_agregation.objects.count()
        print('Y_agregation')
        self.assertEqual(Y_datatest, 0)
        if Y_datatest == 0:
            print('.........OK!')
        else:
            print('.........FAIL!')
class MeasureTest(TestCase):
    def test_measure(self):
        print('UnitTest methode measure()')
        starttest = TableBrut.objects.count()
        print('starttest')
        self.assertEqual(starttest, 0)
        if starttest == 0:
            print('Aucune ligne en base.........OK!')
        else:
            print('.........FAIL!')
        c = Client()
        response = c.post('/alfheimweb/measure/', {'time':'04/17/13','sensor_type':'temp','device_sn':'UnitTest'})
        self.assertEqual(response.status_code, 201)
        if response.status_code != 201:
            print('mauvaise request : 400')
        else:
            print('request POST bonne : 201')
        datatest = TableBrut.objects.count()
        self.assertEqual(datatest, 1)
        if datatest == 1:
            print('une ligne a ete ajoutee.........OK!')
        else:
            print('.........FAIL!')
        
        
        
  #  def test_login(self):
   #     c = Client()
    #    print('username: appert44 password: frey')
     #   print('status code = 200')
      #  self.assertEqual(response.status_code, 200)
       # if response.status_code == 200:
        #    print('.........OK!')
        #else:
       #     print('.........FAIL!')
