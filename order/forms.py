# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from order.models import Order
from order.models import Person

class FormPerson(forms.Form):
    first_name = forms.CharField(label='Имя',  max_length=20)
    last_name = forms.CharField(label='Фамилия',  max_length=20)
    tel_namb = forms.CharField(label='Номер телефона ')
    city = forms.CharField(label='Город', max_length=40)
    email = forms.EmailField(label="Email")


