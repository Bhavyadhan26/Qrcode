from django.shortcuts import render, redirect
from .models import MenuItem, Order, OrderItem


def menu_view(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu_list.html', {'menu_items': menu_items})

def place_order(request):
    if request.method == 'POST':
        order_items = []
        for item in MenuItem.objects.all():
            quantity = int(request.POST.get(f'quantity_{item.id}', 0))
            if quantity > 0:
                order_items.append({'item': item, 'quantity': quantity})

        if order_items:
            # Create the order and redirect to name entry page
            order = Order.objects.create()  # Create a new order
            for order_item in order_items:
                OrderItem.objects.create(
                    order=order, item=order_item['item'], quantity=order_item['quantity']
                )
            # Store the order ID in the session
            request.session['order_id'] = order.id
            return redirect('enter_name')  # Redirect to name entry page

    return redirect('menu_list')  # Redirect back to the menu if no items are selected

def enter_name(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        order_id = request.session.get('order_id')
        
        if order_id:
            order = Order.objects.get(id=order_id)
            order.user_name = user_name  # Save the user's name
            order.save()
            return redirect('order_success')  # Redirect to the success page
    
    return render(request, 'enter_name.html')  # Render the name entry form

def order_success(request):
    order_id = request.session.get('order_id')
    if order_id:
        order = Order.objects.get(id=order_id)
        return render(request, 'order_success.html', {'order': order})
    return redirect('menu_list')

