from django.shortcuts import render

# Create your views here.

def view_basket(request):
    """ A view for the basket """

    return render(request, 'basket/basket.html')