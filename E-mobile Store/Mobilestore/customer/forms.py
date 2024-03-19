from django import forms
from .models import *

class Reviewform(forms.ModelForm):
    class Meta:
        model=Review
        exclude=["user","product"]
        widgets={
            'review':forms.Textarea()
        }
class Cartform(forms.ModelForm):
    class Meta:
        model=CartItem
        fields=["quantity"]
        

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields="__all__"

class CheckOutForm(forms.ModelForm):
    class Meta:
        model=ShippingAddress
        fields="__all__"
