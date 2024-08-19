from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem
from datetime import datetime

def home(request):
    current_year = datetime.now().year
    return render(request, 'home.html', {'current_year': current_year})

def menu(request):
    items = MenuItem.objects.all()
    current_year = datetime.now().year
    context = {
        'items': items,
        'current_year': current_year,
    }
    return render(request, 'menu.html', context)

def menu_item(request, pk):
    current_year = datetime.now().year
    item = get_object_or_404(MenuItem, pk=pk)
    
    context = {
        'item': item,
        'current_year': current_year,
    }
    return render(request, 'menu_item.html', context)

def about(request):
    current_year = datetime.now().year
    return render(request, 'about.html', {'current_year': current_year})

def contact(request):
    current_year = datetime.now().year
    return render(request, 'contact.html', {'current_year': current_year})

def add_to_cart(request, item_id):
    item = get_object_or_404(MenuItem, pk=item_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        
        # Retrieve cart from session or create a new one if it doesn't exist
        cart = request.session.get('cart', {})
        
        # Add or update the item in the cart
        if item_id in cart:
            cart[item_id]['quantity'] += quantity
        else:
            cart[item_id] = {
                'name': item.name,
                'price': str(item.price),
                'quantity': quantity,
                'image': item.image.url,
            }
        
        # Save the cart back to the session
        request.session['cart'] = cart
        
        # Optionally, add a success message
        message = f"{quantity} x {item.name} has been added to your cart."
        
        # Redirect to the same page with a success message
        return render(request, 'add_to_cart.html', {'item': item, 'message': message})
    
    return render(request, 'add_to_cart.html', {'item': item})

def cart(request):
    cart = request.session.get('cart', {})
    total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())
    return render(request, 'cart.html', {'cart': cart, 'total_price': total_price})