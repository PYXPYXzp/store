from django.shortcuts import get_list_or_404, render

from order.models import Person
from order.models import Order
from order.models import Delivery
from products.models import Product
from products.models import Company


def order_tobacco(request):
    detail = Product.objects.get(pk=request.POST.get('product_id'))
    quantity = request.POST['quantity']
    delivery =  get_list_or_404(Delivery)
    # detail = Product.objects.filter(type_product = detail_id)
    # company = Company.objects.filter(pk=comp_id)
    context = {'detail':detail, 'quantity':quantity,'delivery':delivery}
    return render(request, 'order/order_tobak.html', context)