from django.forms import fields
from .models import ShippingAddress
from django import forms

class CheckoutForm(forms.ModelForm):
    name = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id': 'name', 
            'type': 'text',
            'name': 'name',
            'data-constraints': '@Required',
            'placeholder': 'Name...',
        }
    ))
    surname = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id': 'surname', 
            'type': 'text',
            'name': 'surname',
            'data-constraints': '@Required',
            'placeholder': 'Surname...',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs = {
            'class': 'form-input',
            'id': 'email', 
            'type': 'email',
            'name': 'email',
            'data-constraints': '@Email @Required',
            'placeholder': 'Email...',
        }
    ))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id': 'phone', 
            'type': 'text',
            'name': 'phone',
            'data-constraints': '@Numeric @Required',
            'placeholder': 'Contact No...',
        }
    ))
    address= forms.CharField(max_length=100, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id': 'adrress', 
            'type': 'text',
            'name': 'address',
            'data-constraints': '@Required',
            'placeholder': 'Address/Location...',
        }
    ))
    city = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id': 'city', 
            'type': 'text',
            'name': 'city',
            'data-constraints': '@Required',
            'placeholder': 'City/Town...',
        }
    ))
    state = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id': 'state', 
            'type': 'text',
            'name': 'state',
            'data-constraints': '@Required',
            'placeholder': 'Province...',
        }
    ))
    zipcode = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id': 'zipcode', 
            'type': 'text',
            'name': 'zipcode',
            'data-constraints': '@Numeric @Required',
            'placeholder': 'Zip Code...',
        }
    ))
    class Meta:
        model = ShippingAddress
        fields = ['address', 'city', 'state', 'zipcode']