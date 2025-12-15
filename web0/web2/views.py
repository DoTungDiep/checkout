from django.shortcuts import render

def ho(request):
    return render(request, "ho.html")

from django.shortcuts import render, redirect
from .forms import CheckoutForm
from .models import Order, OrderItem


# Dummy cart items for demo (replace with your cart system)
def add_to_cart(request):
    cart = request.session.get("cart", [])
    if request.method == "POST":
        name = request.POST.get("name")
        price = float(request.POST.get("price"))
        qty = int(request.POST.get("qty"))
        
        cart.append({
            "name": name,
            "price": price,
            "qty": qty
        })
        request.session["cart"] = cart
    
    return redirect("checkout")


def checkout(request):
    food = request.GET.get('food')
    price = int(request.GET.get('price'))
    quantity = int(request.GET.get('quantity'))
    total = price * quantity
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            return redirect("confirm")
        else:
            print("INVALID")
            print(form.errors)
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {
        'food': food,
        'price': price,
        'quantity': quantity,
        'total': total,
        'form': form
    })
def success(request):
    return render(request, "success.html")

def confirm(request):
    return render(request,"cf.html")

def list(request):
    return render(request, "list.html")