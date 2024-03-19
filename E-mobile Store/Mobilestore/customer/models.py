from django.db import models
from django.contrib.auth.models import User
from account.models import CustUser
from django.core.exceptions import ValidationError
# Create your models here.

class Product(models.Model):
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name="product",null=True)
    name=models.CharField(max_length=200, null=True)
    price=models.FloatField()
    description=models.CharField(max_length=500,null=True)
    image=models.ImageField(null=True, blank=False)
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class Order(models.Model):
    Customer=models.ForeignKey(CustUser, on_delete=models.SET_NULL, blank=True, null=True)
    data_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False, null=True, blank=False)
    transaction_id=models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    
 
    

class OrderItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity=models.IntegerField(default=0, null=True, blank=False)
    date_added=models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    
class ShippingAddress(models.Model):
    Customer=models.ForeignKey(CustUser, on_delete=models.SET_NULL, blank=True, null=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address=models.CharField(max_length=200, null=True)
    city=models.CharField(max_length=200, null=True)
    state=models.CharField(max_length=200, null=True)
    zipcode=models.CharField(max_length=200, null=True)
    data_added=models.DateTimeField(auto_now_add=True)
    options=(
        ('COD','COD'),
        ('Debit/Credit_Card','Debit/Credit_Card'),
        ('UPI','UPI'))
    payment=models.CharField(max_length=100,choices=options,default='COD')
   

    def __str__(self):
        return self.address

class CartItem(models.Model):
    user = models.ForeignKey(CustUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
    @property
    def get_cart_total(self):
        cartitems = self.orderitem_set.all()
        total = sum([item.get_total for item in cartitems])
        return total
    
    @property
    def get_cart_items(self):
        cartitems = self.orderitem_set.all()
        total = sum([item.quantity for item in cartitems])
        return total

class Review(models.Model):
    review=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    rating=models.FloatField()
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name='revie_user')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='revie_product')
    
    def clean(self):
        if self.rating < 1 or self.rating > 5:
            raise ValidationError("Rating must be between 1 and 5.")