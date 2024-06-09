from django.db import connection
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from shopping.models import CartItem, Cart

from django.contrib import messages

from .models import *
from .forms import *
from shopping.utils import get_cart
from .utils import *


def account_view(request):
    user = request.user 
    client = ClientProfile.objects.filter(account=user).first()
    print(client)
    form = ClientForm(instance=client)
    my_adresses = Address.objects.filter(user=request.user, status=True)
  
    if request.method == "POST":
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
    context = {
        'client': client,
        "form":form,
        "my_adresses":my_adresses,
    }
    return render(request, 'profile/account.html', context)


@login_required(login_url="/account/login/")
def settings_view(request):
    client = ClientProfile.objects.filter(account=request.user).first()
    user = request.user
    if not client:
        form = ClientForm()
        if request.method == "POST":
            form = ClientForm(request.POST, request.FILES)
            if form.is_valid():
                form_data = form.cleaned_data
                client_data = ClientProfile()
                client_data.account = request.user
                client_data.first_name = form_data["first_name"]
                client_data.last_name = form_data["last_name"]
                client_data.email = form_data["email"]
                client_data.phone_number = form_data["phone_number"]
                client_data.image = form_data["image"]
                client_data.save()
                try:
                    user.first_name=form_data['first_name']
                    user.last_name=form_data['last_name']
                    user.email=form_data['email']
                    user.save()
                except:
                    pass
    else:
        form = ClientForm(instance=client)
        if request.method == "POST":
            form = ClientForm(request.POST, request.FILES, instance=client)
            if form.is_valid():
                form.save()
                form_data = form.cleaned_data
                try:
                    user.first_name=form_data['first_name']
                    user.last_name=form_data['last_name']
                    user.email=form_data['email']
                    user.save()
                except:
                    pass

    context = {
        "form":form,
        "user":user,
        "client":client
    }

    return render(request, 'profile/settings.html',  context)


@login_required(login_url="/account/login/")
def adress_view(request):
    my_adresses = Address.objects.filter(user=request.user)
    context = {
        "my_adresses":my_adresses
    }
    return render(request, 'profile/address.html', context)


@login_required(login_url="/account/login/")
def add_adress_view(request):
    form = AdressForm()
    if request.method == "POST":
        form = AdressForm(request.POST)
        if form.is_valid():
            data_full = Address.objects.filter(user=request.user) 
            for i in data_full:
                if i.status == True:
                    i.status = False
                    i.save()
            adres = Address()
            adres.user = request.user
            form_data = form.cleaned_data
            adres.city = form_data['city']
            adres.floor = form_data['floor']
            adres.street = form_data['street']
            adres.country = form_data['country']
            adres.building = form_data['building']
            adres.appertment = form_data['appertment']
            adres.pochta_code = form_data['pochta_code']
            adres.save()
            return redirect(reverse("adress-view"))

    context = {
        "form":form
    }
    return render(request, "profile/add_adress.html", context) 


def update_adress_view(request, pk):
    adres = Address.objects.filter(id=pk)

    if not adres.exists():
        return redirect(reverse("adress-view"))
    else:
        adres = adres.first()

    form = AdressForm(instance=adres)

    if request.method == "POST":
        data = AdressForm(request.POST, instance = adres)
        if data.is_valid():
            data.save()
            return redirect(reverse("adress-view"))

    context = {
        "form":form
    }

    return render(request, "profile/update_adress.html", context) 


def adress_active_view(request, pk, k):
    data_full = Address.objects.filter(user=request.user)
    data = Address.objects.get(id=pk)
    if k=="true":
        for i in data_full:
            i.status=False
            i.save()
        data.status=False
    else:
        for i in data_full:
            i.status=False
            i.save()
        data.status=True
    data.save()
    
    return redirect(reverse("adress-view"))
    

def delete_adress_view(request, pk):
    adres=Address.objects.get(id=pk)
    try:
        adres.delete()
    except:
        pass

    return redirect(reverse("adress-view"))


def selling_view(request):
    return render(request, 'profile/sellings.html')


@login_required(login_url="/account/login/")
def order_view(request, cart_id: int):
    cart = get_object_or_404(Cart, pk=cart_id)
    cart_items = CartItem.objects.filter(cart=cart)
    message = None
    try:
        client = get_object_or_404(ClientProfile, account=request.user)
    except:
        message = "Profil qismini to'ldiring"
        client = None
    try:
        address = get_object_or_404(request.user.address_set, status=True)
    except:
        message = "Address ma'lumotlarini kiriting"
        address = None
    if cart_items and client and address:
        print("cart", cart)
        # Create the OrderSave instance
        order = OrderSave.objects.create(client=client, address=address)
        
        # Create OrderProduct instances
        for item in cart_items:
            OrderProduct.objects.create(order=order, product=item.product, 
                                        quantity=item.quantity, reduced_price_order=item.reduced_price)
        
        # Redirect to the cart page or another appropriate page
        cart.delete()
    if message is not None:
        return redirect('cart-copy', message=message)
    return redirect("cart")



# def my_view(request):
#     # Logic for the view
#     messages.success(request, 'This is a success message.')
#     messages.error(request, 'This is an error message.')
#     return redirect('target_view')