from django.shortcuts import render
from django.http import HttpResponse

from .models import Products

# Create your views here.

def index(request):
    return render(request, 'products/index.html')

def hello_world(request):
    return HttpResponse("Hello, world!")

def product_list(request):
    produtos = Products.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, product_id):
    try:
        produto = Products.objects.get(id=product_id)
        context = {
            'produto': produto
        }
        return render(request, 'products/product_detail.html', context)
    except Products.DoesNotExist:
        return HttpResponse("Produto não encontrado", status=404)