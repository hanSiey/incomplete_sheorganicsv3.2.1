from shopping.models import *
from .models import *
from django import forms

class UpdateForm_two(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']

class UpdateForm_three(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['status']

class CreateUser(forms.Form):
    name = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs = {
            'class': 'input100', 
            'type': 'text',
            'name': 'name',
            'data-constraints': '@Required',
        }
    ))
    surname = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs = {
            'class': 'input100', 
            'type': 'text',
            'name': 'surname',
            'data-constraints': '@Required',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs = {
            'class': 'input100',
            'type': 'email',
            'name': 'email',
            'data-constraints': '@Email @Required',
        }
    ))
    phone = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'input100',
            'type': 'phone',
            'name': 'phone',
            'data-constraints': '@Required',
        }
    ))
    password1 = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs = {
            'class': 'input100',
            'type': 'password',
            'name': 'password1',
            'data-constraints': '@Required',
        }
    ))
    password2 = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs = {
            'class': 'input100', 
            'type': 'password',
            'name': 'password2',
            'data-constraints': '@Required',
        }
    ))

class LogInForm(forms.Form):
    name = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs = {
            'class': 'input100', 
            'type': 'text',
            'name': 'name',
            'data-constraints': '@Required',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs = {
            'class': 'input100',
            'type': 'email',
            'name': 'email',
            'data-constraints': '@Email @Required',
        }
    ))
    password1 = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs = {
            'class': 'input100',
            'type': 'password',
            'name': 'password1',
            'data-constraints': '@Required',
        }
    ))

class CreateDisForm(forms.ModelForm):
    name = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs = {
            'class': 'form-control', 
            'type': 'text',
            'name': 'name',
            'data-constraints': '@Required',
            'placeholder':'Name',
        }
    ))
    surname = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs = {
            'class': 'form-control', 
            'type': 'text',
            'name': 'surname',
            'data-constraints': '@Required',
            'placeholder':'Surname',
        }
    ))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs = {
            'class': 'form-control', 
            'type': 'text',
            'name': 'phone',
            'data-constraints': '@Required',
            'placeholder':'Phone',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs = {
            'class': 'form-control',
            'type': 'email',
            'name': 'email',
            'data-constraints': '@Email @Required',
            'placeholder':'Email',
        }
    ))
    area_of_operation = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs = {
            'class': 'form-control', 
            'type': 'text',
            'name': 'location',
            'data-constraints': '@Required',
            'placeholder':'Area of opreration',
        }
    ))
    class Meta:
        model = Distributor
        fields = '__all__'

class ProductsForm(forms.ModelForm):
    name = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs = {
            'class': 'form-control', 
            'type': 'text',
            'name': 'name',
            'data-constraints': '@Required',
            'placeholder':'Name',
        }
    ))
    measurement = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs = {
            'class': 'form-control', 
            'type': 'text',
            'name': 'measurement',
            'data-constraints': '@Required',
            'placeholder':'Measurement',
        }
    ))
    price = forms.IntegerField(widget=forms.NumberInput(
        attrs = {
            'class': 'form-control', 
            'type': 'number',
            'name': 'price',
            'data-constraints': '@Required',
            'placeholder':'Price',
        }
    ))
    image = forms.ImageField(widget=forms.ClearableFileInput(
        attrs = {
            'class': 'form-control', 
            'type': 'file',
            'name': 'image',
            'data-constraints': '@Required',
        }
    ))
    class Meta:
        model = Product
        fields = '__all__'

class messageform(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs = {
            'class': 'form-input',
            'id': 'contact-name', 
            'type': 'text',
            'name': 'name',
            'data-constraints': '@Required',
        }
    ))
    surname = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs = {
            'class': 'form-input',
            'id': 'contact-sec-name', 
            'type': 'text',
            'name': 'sec-name',
            'data-constraints': '@Required',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs = {
            'class': 'form-input',
            'id': 'contact-email', 
            'type': 'email',
            'name': 'email',
            'data-constraints': '@Email @Required',
        }
    ))
    phone = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs = {
            'class': 'form-input',
            'id': 'contact-phone', 
            'type': 'text',
            'name': 'phone',
            'data-constraints': '@Numeric @Required',
        }
    ))
    message = forms.CharField(max_length=1000, widget=forms.Textarea(
        attrs = {
            'class': 'form-input',
            'id': 'contact-message', 
            'type': 'text',
            'name': 'message',
            'data-constraints': '@Required',
        }
    ))
    class Meta:
        model = OnlineContact
        fields = '__all__'

