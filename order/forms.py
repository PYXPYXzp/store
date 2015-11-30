__author__ = 'artem'
# -*- coding: utf-8 -*-
from django import forms
from .models import Person

class FormPerson(forms.Form):
    first_name = forms.CharField(label='Имя',  max_length=20)
    last_name = forms.CharField(label='Фамилия',  max_length=20)
    tel_namb = forms.CharField(label='Номер телефона ')
    city = forms.CharField(label='Город', max_length=40)
    email = forms.EmailField(label="Email")

# class DetailOrder(forms.Form):
#      # date_order = forms.DateTimeField(auto_now=True, auto_now_add=False)
