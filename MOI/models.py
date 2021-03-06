from django.db import models
import datetime
from django.utils import timezone

class Employee(models.Model):
    emp_name = models.CharField(max_length=200)
    devision = models.CharField(max_length=200)
    emp_phon = models.IntegerField()


    
    def __str__(self):

        return self.emp_name



class Tender(models.Model):

    employee = models.ForeignKey(Employee)
    ten_num = models.CharField('Tender_nuumber',max_length=100)
    date_received = models.DateTimeField('Received on')
    band_num = models.IntegerField()
    purch_order_number = models.IntegerField()
    contract_num = models.CharField('contract_number',max_length=200)
    date_closed = models.DateTimeField('closing date')



    def __str__(self):
        return self.ten_num


