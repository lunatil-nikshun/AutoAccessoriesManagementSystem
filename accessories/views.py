import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.shortcuts import render
from django.db.models import Q
from .models import Accessories, CartItems, Cart
from .forms import PartForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




# Create your views here.
def home(request):
    return render(request, 'accessories/home.html')

def registration(request):
    return render(request, 'accessories/registration.html')

def part_list(request):
    accessories = Accessories.objects.all()
    return render(request, 'accessories/accessories_list.html', {'accessories' : accessories })

def part_detail(request, pk):
    #accessories = get_object_or_404(Accessories, pk=pk)
    accessories = Accessories.objects.filter(pk=pk)
    return render(request, 'accessories/part_detail.html', {'accessories': accessories})


def part_create(request):
    if request.method == 'POST':
        form = PartForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('part_list')
    else:
        form = PartForm()
    return render(request, 'accessories/part_create.html', {'form' : form})

def my_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            pass
    return render(request, 'accessories/login.html')

def my_logout(request):
    logout(request)
    return redirect('my_login')

def add_to_cart(request, pk):
    if request.method == 'POST':
        accessories = get_object_or_404(Accessories, pk=pk)
        quantity = int(request.POST.get('quantity', 1))
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItems.objects.get_or_create(cart=cart, accessories=accessories, defaults={'quantity': quantity})
        
        #the cart is initially empty
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        else:
            cart_item.quantity = quantity
            cart_item.save()
        return redirect('cart')


def cart_view(request): 
    cart_items = CartItems.objects.filter(cart__user=request.user)
    total_amount = sum(item.accessories.price * item.quantity for item in cart_items)
    return render(request, 'accessories/cart.html', { 'cart_items' : cart_items, 'total_amount' : total_amount })

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItems, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')

def search_results(request):
    search_query = request.GET.get('search', '')
    accessories = Accessories.objects.filter(name__icontains=search_query)
    return render(request, 'accessories/search_results.html', {'accessories' : accessories, 'search_query' : search_query})

def search_results_car(request):
    search_query = request.GET.get('car_search', 'car')
    accessories = Accessories.objects.filter(name__icontains=search_query)
    return render(request, 'accessories/home_car.html', {'accessories' : accessories, 'search_query' : search_query})

def search_results_bike(request):
    search_query = request.GET.get('car_search', 'bike')
    accessories = Accessories.objects.filter(name__icontains=search_query)
    return render(request, 'accessories/home_bike.html', {'accessories' : accessories, 'search_query' : search_query})

def search_results_cycle(request):
    search_query = request.GET.get('car_search', 'cycle')
    accessories = Accessories.objects.filter(name__icontains=search_query)
    return render(request, 'accessories/home_cycle.html', {'accessories' : accessories, 'search_query' : search_query})

def proceed_to_pay(request):
    cart_items = CartItems.objects.filter(cart__user=request.user)
    total_amount = sum(item.accessories.price * item.quantity for item in cart_items)
    return render(request, 'accessories/proceed_to_pay.html', {'total_amount': total_amount})

@csrf_exempt
def payment_confirmation(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItems.objects.filter(cart=cart)
    order_amount = 0

    total_amount = sum(item.accessories.price * item.quantity for item in cart_items)
    client = razorpay.Client(auth=(settings.RAZORPAY_TEST_KEY_ID, settings.RAZORPAY_TEST_KEY_SECRET))

    order_amount = (order_amount + total_amount) * 100
    order_currency = 'INR'
    
    order = client.order.create({'amount':order_amount, 'currency':order_currency})

    context = {'order_amount': order_amount, 'order': order, 'razorpay_key_id': settings.RAZORPAY_TEST_KEY_ID}
    return render(request, 'accessories/payment_confirmation.html', context)