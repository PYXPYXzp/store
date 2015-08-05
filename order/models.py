from django.db import models

class Delivery (models.Model):
    type_delivery = models.CharField(max_length=200, null=True, blank=True)

class Person (models.Model):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    tel_namb = models.IntegerField(default=0, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    email = models.EmailField()

class Order (models.Model):
    date_order = models.DateTimeField('date published')
    delivery = models.ForeignKey(Delivery)
    person = models.ForeignKey(Person)
    total_cost = models.IntegerField(default=0, null=True, blank=True)
    

