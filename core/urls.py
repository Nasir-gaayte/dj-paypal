from django import views
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('payment_done/',views.payment_done, name='payment_done'),
    path('payment_cancelled/',views.payment_cancelled, name='payment_cancelled'),
]
