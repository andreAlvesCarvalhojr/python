from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_list_view, name='product_list'),
    path('products-create', views.product_create_view, name='create_product'),
]
