from typing import List
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from shopping.models import *
from .models import *
from .filters import orderFilter
from django.contrib.auth.models import Group, User, auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_user, admin_only
import json

# Create your views here.

@unauthenticated_user
def register(request):
    if request.method == 'POST':
        create_user_form = CreateUser(request.POST)

        if create_user_form.is_valid():
            name = create_user_form.cleaned_data.get('name')
            surname = create_user_form.cleaned_data.get('surname')
            email = create_user_form.cleaned_data.get('email')
            phone = create_user_form.cleaned_data.get('phone')
            password1 = create_user_form.cleaned_data.get('password1')
            password2 = create_user_form.cleaned_data.get('password2')

            if password1 == password2:
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'Email Already exists')
                    return redirect('register')
                elif User.objects.filter(username=name, email=email).exists():
                    messages.info(request, 'User Already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=name, email=email,first_name=name, last_name=surname, password=password1)
                    user.save()
                    
                    group = Group.objects.get(name="customer")
                    user.groups.add(group)
                
                new_user = User.objects.get(email=email)
                Customer.objects.create(
                    user=new_user,
                    name=new_user.first_name,
                    surname=new_user.last_name,
                    email=new_user.email,
                    phone=phone,
                )
                messages.info(request, "Account successfully created")
                return redirect('login')
            else:
                messages.info(request, 'Passwords Do Not Match')
                return redirect('register')
    else:
        create_user_form = CreateUser() 
    return render(request, 'register.html', {'form':create_user_form})

@unauthenticated_user
def login(request):
    if request.method == 'POST':
        login_form = LogInForm(request.POST)

        username = request.POST.get('name')
        email =request.POST.get('email')
        password =request.POST.get('password1')

        user = authenticate(request, username=username, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            if user.is_superuser:
                return redirect('dashboard')
            else:
                return redirect('/')
        else:
            messages.info(request, 'Credentails invalid')
            return redirect('login')     
    else:
        login_form = LogInForm()
    return render(request, 'login.html', {'form':login_form})
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contacts(request):
    if request.method == 'POST':
        message_form = messageform(request.POST)
        if message_form.is_valid():
            message_form.save()
            return redirect('message_success')
        else:
            messages.info(request, "Enter valid information")
            return redirect('contacts')
    else:
        message_form = messageform()
    return render(request, "contacts.html", {'message_form':message_form})

def message_success(request):
    return render(request, "message_success.html")
    
@login_required(login_url='login')
@admin_only
def dashboard(request):
    orders = Order.objects.all()
    customer = Customer.objects.all()
    distributors = Distributor.objects.all()
    message = OnlineContact.objects.all()

    total_customers = customer.count()
    total_messages = message.count()
    total_orders = orders.filter(complete=True).count()
    total_distributors = distributors.count()
    pending = orders.filter(complete=True, status='Pending').count()
    total_d = orders.filter(complete=True, status='Delivered').count()
    out_on_d = orders.filter(complete=True, status='Out on delivery').count()
        


    context = { 
        'orders':orders.filter(complete=True).order_by('-id'),
        'total_orders':total_orders,
        'total_customers': total_customers,
        'total_distributors': total_distributors,
        'total_messages': total_messages,
        'total_d': total_d,
        'pending': pending,
        'out_on_d':out_on_d,
        }
    return render(request, "admin_panel/dashboard.html", context)

def distributors(request):
    distributors = Distributor.objects.all().order_by('-id')
    return render(request, "admin_panel/distributors_table.html", {'distributors':distributors})


def products(request):
    products = Product.objects.all().order_by('-id')
    return render(request, "admin_panel/products_table.html", {'products':products})

def customerMessages(request):
    message = OnlineContact.objects.all().order_by('-id')
    return render(request, "admin_panel/messages_table.html", {'message':message})

@login_required(login_url='login')
@admin_only
def  CreateDistributor(request):
    if request.method == "POST":
        createDis_form = CreateDisForm(request.POST)
        if createDis_form.is_valid():
            email = createDis_form.cleaned_data.get('email')
            if Distributor.objects.filter(email=email).exists():
                    messages.info(request, "Email Already Exits")
                    return redirect('add_distributor')
            else:
                    createDis_form.save()
                    return redirect('distributors')
        else:
            messages.info(request, "Invaild data entered")
            return redirect('add_distributor')
    else:
        createDis_form = CreateDisForm()
        
    context = {
        'form':createDis_form
    }
    return render(request, "admin_panel/add_distributor.html", context)

@login_required(login_url='login')
@admin_only
def AddProduct(request):
    if request.method == 'POST':
        product_form = ProductsForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('products')
        else:
            messages.info(request, "Invaild data")
            return redirect('add_product')
    else:
        product_form = ProductsForm()
        
    context = {
        'form': product_form
    }
    return render(request, "admin_panel/add_product.html", context)

@login_required(login_url='login')
def customerDashboard(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all().filter(complete=True).order_by('-id')
    orders_count = orders.count()

    myfilter = orderFilter(request.GET, queryset=orders)
    orders = myfilter.qs
    context = {
        'customer':customer,
        'orders':orders,
        'orders_count': orders_count,
        'myfilter':myfilter,
        }
    return render(request, "customer.html", context)
    
def customers_table(request):
    customers = Customer.objects.all().order_by('-id')
    return render(request, "admin_panel/customers_table.html", {'customers':customers})

def CustomerViewOrder(request, pk):
    order = Order.objects.get(id=pk)
    order_total_amount = order.get_cart_total
    order_items = order.orderitem_set.all()
    shippingaddress = order.shippingaddress_set.all()


    context ={
        'order':order,
        'order_items':order_items,
        'total':order_total_amount,
        'addresses':shippingaddress,
    }     
    return render(request, "view_order.html", context)

def ViewOrder(request, pk):
    order = Order.objects.get(id=pk)
    order_total_amount = order.get_cart_total
    order_items = order.orderitem_set.all()
    shippingaddress = order.shippingaddress_set.all()

    if request.method == 'POST':
        update_form = UpdateForm_two(request.POST, instance=order)
        update_form.save()
        return redirect('dashboard')
    else:
        update_form = UpdateForm_two(instance=order)

    context ={
        'order':order,
        'order_items':order_items,
        'total':order_total_amount,
        'addresses':shippingaddress,
        'update_form':update_form,
    }     
    return render(request, "admin_panel/view_order.html", context)

def ViewProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        update_form = UpdateForm_three(request.POST, instance=product)
        update_form.save()
        return redirect('products')
    else:
        update_form = UpdateForm_three(instance=product)
    
    context = {
        'update_form':update_form,
        'product':product,
    }
    return render(request, "admin_panel/view_product.html", context)

def ViewCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all().filter(complete=True).order_by('-id')
    orders_count = orders.count()

    context = {
        'customer':customer,
        'orders':orders,
        'orders_count': orders_count,
        }
    return render(request, "admin_panel/view_customer.html", context)

def ViewMessage(request, pk):
    single_message = OnlineContact.objects.get(id=pk)
    return render(request, "admin_panel/view_message.html", {'message':single_message})


def deleteDistributor(request, pk):
	distributor = Distributor.objects.get(id=pk)
	distributor.delete() 
	return redirect('distributors')
    

def deleteCustomer(request, pk):
	customer = Customer.objects.get(id=pk)
	customer.delete()
	return redirect('customers')

def delete_Order(request, pk):
	order = Order.objects.get(id=pk)
	order.delete()
	return redirect('/')

def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	order.delete()
	return redirect('orders')

def deleteProduct(request, pk):
	product = Product.objects.get(id=pk)
	product.delete()
	return redirect('products')

def deleteMessage(request, pk):
    single_message = OnlineContact.objects.get(id=pk)
    single_message.delete()
    return redirect('messages')


