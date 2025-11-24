from urllib import request
from django.shortcuts import redirect, render
from .models import Product
from .forms import ProductForm

# Create your views here.
def product_list_view(request):
    produtos = Product.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'product/product_list.html', context)

def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
        
    return render(request, 'product/product_create.html', {'form': form})