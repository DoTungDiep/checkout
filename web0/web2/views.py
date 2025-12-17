from django.shortcuts import render

def ho(request):
    return render(request, "ho.html")

from django.shortcuts import render, redirect
from .forms import CheckoutForm
from .models import Order, OrderItem


# Dummy cart items for demo (replace with your cart system)
def checkout(request):
    food = request.GET.get('food',)
    price = int(request.GET.get('price',))
    quantity = int(request.GET.get('quantity',))
    food1 = request.GET.get('food1')
    price1 = int(request.GET.get('price1',))
    quantity1 = int(request.GET.get('quantity1',))
    total = (price * quantity)+(price1 * quantity1) 
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
        'form': form,
        'food1':food1,
        'price1': price1,
        'quantity1':quantity1
    })
def success(request):
    return render(request, "success.html")

def confirm(request):
    return render(request,"cf.html")

def list(request):
    return render(request, "list.html")