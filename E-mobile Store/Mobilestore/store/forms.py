from django import forms
from customer.models import Product
from account.models import CustUser


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=["name","description","price","image"]
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(),
            "description":forms.TextInput(),
            "image":forms.FileInput(),
        }




