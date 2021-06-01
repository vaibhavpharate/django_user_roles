from .models import Order,Customer,Category,Tag,Product
from django.forms import ModelForm

# user creation form and model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer','product','order_status']

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
