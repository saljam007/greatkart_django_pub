from django.shortcuts import render
from store.models import Product


def home(request):
    products = Product.objects.all().filter(is_available=True) #this will only show products that are available when you use this .filter function
    
    context = {
        'products': products,
    }
    return render(request, 'home.html', context)