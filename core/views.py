import uuid
from decimal import Decimal

from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm


def home(request):
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '20.00', 
        'item_name': 'product 1',
        'invoice': str(uuid.uuid1()),
        'currency_code': 'USD',
        'notify_url': f'http://{host}{reverse("paypal-ipn")}',
                                           
        'return_url': f'http://{host}{reverse("payment_done")}',
                                          
        'cancel_return': f'http://{host}{reverse("payment_cancelled")}',
    }                                       
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render (request,'core/home.html',{'form':form})


def payment_done(request):
    messages.success(request,'well done *****')
    return redirect('home')


def payment_cancelled(request):
    messages.info(request,'payed cancelled')
    return redirect('home')