from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Topping, Veg_Pizza,NonVeg_Pizza, Cart, Orders


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    v_pizzas = Veg_Pizza.objects.all()
    n_pizzas = NonVeg_Pizza.objects.all()
    toppings = Topping.objects.all()
    context = {
        "v_pizzas": v_pizzas,
        "n_pizzas": n_pizzas,
        "toppings": toppings,
        "user": request.user
    }
    return render(request, "orders/index.html", context)


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    if '@' in username:
        username = User.objects.get(email=username.lower()).username
        user = authenticate(request, username=username, password=password)
    else:
        user = authenticate(request, username=username, password=password)
    if user:
        print("login")
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials"})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
    # return render(request, "orders/login.html", {"message": "Logout successfully "})


def register(request):
    return render(request, "orders/register.html")


def registered(request):
    username = request.POST.get("usernam")
    email = request.POST.get("emai").lower()
    password = request.POST.get("passwor")
    User.objects.create_user(f"{username}", f"{email}", f"{password}")
    return render(request, "orders/login.html")


# views for home page
def add_items(request, pizza_name, regular,medium, large):
    item = pizza_name
    size_r = regular
    size_m = medium
    size_l = large
    toppings = Topping.objects.all()
    context = {
        "item": item,
        "size_r": size_r,
        "size_m": size_m,
        "size_l": size_l,
        "toppings": toppings
    }
    return render(request, "orders/add_items.html", context)


def add_to_cart(request, item):
    name = item
    price = request.POST.get("size")
    extras = request.POST.get("extras")
    extras_price = Topping.objects.get(name=extras).price
    price = str(float(price) + float(extras_price))
    c = Cart(item=name, price=price, extras=extras)
    c.save()
    c.user.set([request.user])
    return HttpResponseRedirect(reverse("index"))


def show_cart(request):
    cart = Cart.objects.filter(user=request.user)

    context = {
        "cart": cart,
        "user": request.user.username
    }
    return render(request, "orders/cart.html", context)


def place_order(request, item, price, extras, pk):
    order = Orders(item=item, price=price, extras=extras)
    order.save()
    order.user.set([request.user])
    Cart.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse("index"))

def delete_order(request, pk):
    Cart.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse("index"))

def view_orders(request):
    orders = Orders.objects.all()
    context = {
        "orders": orders
    }
    return render(request, "orders/view_orders.html", context)
