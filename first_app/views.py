from django.shortcuts import render, redirect

from django.contrib import messages

## user defined imports
from .models import Product, Customer, Order
from .form_data import CustomerForm, OrderForm, UserRegisterForm
from .decorators import un_auth_user, allowed_users, customer_only

## user logins and logouts
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
@login_required(login_url='login_user')
@allowed_users(allowed_roles=['admins'])
# @customer_redirect
def index(request):
    all_orders = Order.objects.all()
    customers = Customer.objects.all()

    total = Order.objects.all().count()
    pending = Order.objects.filter(order_status="PENDING").count()
    delivered = Order.objects.filter(order_status="DELIVERED").count()
    shipping = Order.objects.filter(order_status="SHIPPING").count()

    context = {'orders':all_orders,'customers':customers,
               'total':total,'pending':pending,'delivered':delivered,
               'shipping':shipping}
    return render(request,'first_app/index.html',context=context)

@login_required(login_url='login_user')
@allowed_users(allowed_roles=['admins'])
def add_customer(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Customer Successfully Added")
            return redirect('home')
        else:
            messages.warning(request,"Some Error Occurred")
    context = {'form':form}
    return render(request,'first_app/add_customer.html',context=context)

@login_required(login_url='login_user')
@allowed_users(allowed_roles=['admins'])
def add_order(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Order Successfully Added")
            return redirect('home')
        else:
            messages.warning(request,"Some Error Occurred")
    context = {'form':form}
    return render(request,'first_app/add_order.html',context=context)

@login_required(login_url='login_user')
def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()

    total = orders.count()
    pending = orders.filter(order_status="PENDING").count()
    delivered = orders.filter(order_status="DELIVERED").count()
    shipping = orders.filter(order_status="SHIPPING").count()

    context = {'customer':customer,'orders':orders,
               'total':total,'pending':pending,'delivered':delivered,
               'shipping':shipping}
    return render(request,'first_app/customer.html',context=context)

@login_required(login_url='login_user')
@allowed_users(allowed_roles=['admins'])
def update_order(request,pk):
    order = Order.objects.get(id=pk)
    order_form = OrderForm(instance=order)

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Order Updated Successfully")
            return redirect('home')
        else:
            messages.error(request,"Some Error Occurred")
    context = {'form':order_form}
    return render(request,'first_app/update_order.html',context=context)

@login_required(login_url='login_user')
def delete_order(request,pk):
    order = Order.objects.get(id=pk)
    order.delete()
    messages.info(request,"Order Remove Successfully")
    return redirect('home')

def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get('username')
            user = form.save()
            group = Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request,'User Registered Successfully')
            return redirect('home')
        else:
            messages.warning(request,"Some Error Occurred")
    context = {'form':form}
    return render(request,'first_app/register.html',context=context)

@un_auth_user
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        passsword = request.POST.get('password')

        if username is not None:
            user = authenticate(request,username=username,password=passsword)
            if user is not None:
                login(request, user)
                if user.groups.all()[0].name == "admins":
                    messages.success(request,"Admin Login Successful")
                    return redirect('home')
                elif user.groups.all()[0].name == "customer":
                    messages.success(request,"Customer Login Successful")
                    return redirect('user_profile')


            else:
                messages.error(request,'Login Uncessful')
    return render(request,'first_app/login_user.html')

@login_required(login_url='login_user')
def logout_user(request):
    if request.user.username:
        logout(request)
        messages.info(request,"Logout Successful")
        return redirect('login_user')
    else:
        messages.warning(request,"No user Logged In")
        return redirect('login_user')

@login_required(login_url='login_url')
@customer_only
def user_profile(request):
    customer_id = request.user.customer.id;
    customer = Customer.objects.get(id=customer_id)
    orders = request.user.customer.order_set.all()
    total = orders.count()
    pending = orders.filter(order_status="PENDING").count()
    delivered = orders.filter(order_status="DELIVERED").count()
    shipping = orders.filter(order_status="SHIPPING").count()
    print("Hello user")
    context = {'customer':customer,'orders':orders,
               'total':total,'pending':pending,'delivered':delivered,
               'shipping':shipping}
    return render(request,'first_app/user_profile.html',context=context)
