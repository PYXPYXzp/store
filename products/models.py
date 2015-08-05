from django.db import models

class Type (models.Model):
    type_product = models.CharField(max_length=200, null=True, blank=True)

class Units(models.Model):
    type_units = models.CharField(max_length=200, null=True, blank=True)

class Product (models.Model):
    image = models.ImageField()
    type = models.ForeignKey(Type)
    company = models.CharField(max_length=200, null=True, blank=True)
    model = models.CharField(max_length=200, null=True, blank=True)
    flower = models.CharField(max_length=200, null=True, blank=True)
    weight_tobacco = models.IntegerField(default=0, null=True, blank=True)
    height_shisha = models.IntegerField(default=0, null=True, blank=True)
    type_bowls = models.CharField(max_length=200, null=True, blank=True)
    units = models.ForeignKey(Units,null=True, blank=True)
    cost = models.IntegerField(default=0, null=True, blank=True)
    characteristics = models.TextField(null=True, blank=True)
    specification = models.TextField(null=True, blank=True)