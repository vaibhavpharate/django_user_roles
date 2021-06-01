from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('add_customer',views.add_customer,name="add_customer"),
    path('add_order',views.add_order,name="add_order"),
    path('customer/<int:pk>',views.customer,name='customer'),
    path('update_order/<int:pk>',views.update_order,name='update_order'),
    path('delete_order/<int:pk>',views.delete_order,name='delete_order'),
    path('register',views.register,name='register'),
    path('login_user',views.login_user,name="login_user"),
    path('logout',views.logout_user,name="logout"),
    path('user_profile',views.user_profile,name="user_profile")
]
