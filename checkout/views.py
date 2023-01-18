from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There are no products in your basket")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MRcnpEOlH4sOO4CYjWmI3TDUyXGJ2jUI96lLnTbn8hVMWi8yJSY9SeIF45vsVkKy2Q6huNpLAYA5iLA4wylcgMq00XacWfDP0',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

    