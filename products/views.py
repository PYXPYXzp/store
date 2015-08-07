from django.shortcuts import render

from django.http import HttpResponse
from .models import Type


def index(request):
    type_product = Type.objects.all()
    context = {'type_product':type_product}
    return render(request, 'tobaccostore/index.html', context)