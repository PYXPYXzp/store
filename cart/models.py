from django.db import models
from products.models import Product
from django.forms import ModelForm


class CartItem(models.Model):
    cart_id = models.CharField(max_length=150)
    date = models.DateField(auto_now=True, auto_now_add=False)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    product = models.ForeignKey(Product, unique=False)

    class Meta:
        ordering = ['date']

    @property
    def total(self):
        return self.quantity * self.product.cost

    @property
    def name(self):
        return self.product.name

    @property
    def price(self):
        return self.product.cost

    @property
    def augment_quantity(self, quantity):
         self.quantity = self.quantity + int(quantity)
         self.save()