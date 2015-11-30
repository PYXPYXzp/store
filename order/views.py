from django.shortcuts import get_list_or_404, render, redirect


from order.models import Person
from order.models import Order
from order.models import Delivery
from products.models import Product
from products.models import Company
from .forms import FormPerson



def order(request):
    detail = Product.objects.get(pk=request.POST.get('product_id'))
    quantity = request.POST['quantity']
    delivery =  get_list_or_404(Delivery)
    if request.method == 'POST':
        form = FormPerson(request.POST)
    context = {'detail':detail, 'quantity':quantity,'delivery':delivery,'form':form}
    return render(request, 'order/order_tobak.html', context)


def add_info(request):
     if request.method == 'POST':
        form = FormPerson(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            tel_namb = form.cleaned_data['tel_namb']
            comment = form.cleaned_data['comment']
            city = form.cleaned_data['city']
            Person.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                tel_namb = tel_namb,
                comment = comment,
                city = city,
                )
            Order.objects.create(
                
            )
            return redirect('http://127.0.0.1:8000/index/')
