from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

# to redirect to home if user is logged in
def un_auth_user(view_func):
    def wrapped_function(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapped_function

## after authenticating check the role
def allowed_users(allowed_roles=[]):
    def decorator_wr(view_func):
        def wrapped_function(request,*args,**kwargs):
            group = None ## to get role from user
            # print(allowed_roles)
            print(allowed_roles)
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            else:
                group = "customer"
            if group == "admins":
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse("You are not allowed to access this Page")
        return wrapped_function
    return decorator_wr

def customer_only(view_func):
    def wrapped_function(request,*args,**kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == "customer":
            return view_func(request,*args,**kwargs)
        else:
            return HttpResponse("Admins Cannot access user profile")
    return wrapped_function
# def customer_redirect(view_func):
#     def wrapped_function(request,*args,**kwargs):
#         group = None
#         if request.user.groups.exists():
#             group =  request.user.groups.all()[0].name
#         if group == "admins":
#             return view_func(request,*args,**kwargs)
#         elif group == "customer":
#             return redirect('customer', '1')
#         else:
#             return redirect('login')
#     return wrapped_function
