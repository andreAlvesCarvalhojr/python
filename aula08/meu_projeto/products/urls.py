from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.product_list, name='product_list'),
    path('detail/<int:product_id>/', views.product_detail, name='product_detail'),
]