from django.db import models
from products.models import Product
from django.forms import ModelForm
from cart.models import CartItem


class Delivery (models.Model):
    type_delivery = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.type_delivery

class Person (models.Model):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    tel_namb = models.IntegerField(default=0, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    email = models.EmailField()

class Order (models.Model):
    delivery = models.ForeignKey(Delivery)
    person = models.ForeignKey(Person)
    order = models.ForeignKey(CartItem)


class DetailOrder(ModelForm):
     class Meta:
         model = Order
         fields = ['delivery', 'person']

def __unicode__(self):
                   return self.type_delivery