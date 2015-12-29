from django.db import models

class Type (models.Model):
    type_product = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.type_product

class Units(models.Model):
    type_units = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.type_units

class Company(models.Model):
    name_company = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.name_company

class Product (models.Model):
    image = models.ImageField()
    type = models.ForeignKey(Type, null=True, blank=True)
    company = models.ForeignKey(Company, null=True, blank=True)
    model = models.CharField(max_length=200, null=True, blank=True)
    flower = models.CharField(max_length=200, null=True, blank=True)
    weight_tobacco = models.IntegerField(default=0, null=True, blank=True)
    height_shisha = models.IntegerField(default=0, null=True, blank=True)
    type_bowls = models.CharField(max_length=200, null=True, blank=True)
    units = models.ForeignKey(Units,null=True, blank=True)
    cost = models.IntegerField(default=0, null=True, blank=True)
    characteristics = models.TextField(null=True, blank=True)
    specification = models.TextField(null=True, blank=True)


    def __unicode__(self):
        return self.characteristics
    def __unicode__(self):
        return unicode(self.type)
    def __unicode__(self):
        return unicode(self.units)


class Bal_program(models.Model):
    bal = models.IntegerField()
    date = models.DateField(auto_now=True, auto_now_add=False)
