from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from telebot.sandmessage import send_telegram


def first_page(request):
    slider_list = CmsSlider.objects.all()
    try:
        pc_1 = PriceCard.objects.get(pk=1)
    except:
        pc_1 = '100'
    try:
        pc_2 = PriceCard.objects.get(pk=2)
    except:
        pc_2 = '2000'
    try:
        pc_3 = PriceCard.objects.get(pk=3)
    except:
        pc_3 = '30000'
    price_table = PriceTable.objects.all()
    form = OrderForm()
    dict_obj = {'slider_list': slider_list,
                'pc_1': pc_1,
                'pc_2': pc_2,
                'pc_3': pc_3,
                'price_table': price_table,
                'form': form,
                }
    return render(request, './index.html', dict_obj)


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name=name, order_phone=phone)
        element.save()
        send_telegram(tg_name=name, tg_phone=phone)
        return render(request, './thanks.html', {
            'name': name,
            'phone': phone
        })
    else:
        return render(request, './thanks.html')
