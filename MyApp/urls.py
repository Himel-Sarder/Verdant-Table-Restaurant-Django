from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('menu/<int:pk>/', views.menu_item, name='menu_item'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    

]
