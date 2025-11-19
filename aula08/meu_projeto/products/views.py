from django.shortcuts import render
from django.http import HttpResponse

from .models import Products

# Create your views here.

def index(request):
    return HttpResponse("Bem-vindo à página de produtos!")

def hello_world(request):
    return HttpResponse("Hello, world!")

def product_list(request):
    produtos = Products.objects.all()
    str_produtos = ", ".join([produto.name for produto in produtos])
    return HttpResponse(f"Lista de produtos disponíveis: {str_produtos}")