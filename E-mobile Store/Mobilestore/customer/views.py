from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,View,FormView
from .models import *
from django.db.models import Q
from django.contrib import messages
from .forms import *
# Create your views here.

class CustHome(TemplateView):
    template_name="chome.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['products']=Product.objects.all()
        return context
    
class ProductDetails(FormView):
    template_name="prodetails.html"
    form_class=Reviewform
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] =Product.objects.get(id=self.kwargs.get('pid'))
        context["review"] =Review.objects.all()
        return context

class CartView(TemplateView):
    template_name="cart.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['cartitems']=CartItem.objects.filter(user=self.request.user)
        cartitems = CartItem.objects.filter(user=self.request.user)
        total = 0
        item = 0
        for cart_item in cartitems:
            total += (cart_item.product.price * cart_item.quantity)
            item += (cart_item.quantity)
        context['grand_total']=total
        context['item_count']=item
        return context

class OrderPro(CreateView):
    model=Order
    form_class=OrderForm
    template_name='order.html'
    
    success_url=reverse_lazy('products')

class AddCart(CreateView):
    template_name="addcart.html"
    form_class=Cartform
    model=CartItem
    success_url=reverse_lazy("cart")
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['pro']=Product.objects.get(id=self.kwargs.get("pid"))
        return context
    def form_valid(self, form):
        form.instance.user=self.request.user
        form.instance.product=Product.objects.get(id=self.kwargs.get("pid"))
        self.object=form.save()
        return super().form_valid(form)


class CheckView(CreateView):
    template_name="checkout.html"
    model=ShippingAddress
    form_class=CheckOutForm
    success_url=reverse_lazy("order")
    def form_valid(self,form):
        form.instance.user=self.request.user
        self.objects=form.save()
        messages.success(self.request,"Purchased!!")
        return super().form_valid(form)

class DeleteCart(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pid')
        cart=CartItem.objects.get(id=id)
        cart.delete()
        return redirect("cart")
    
class Add_review(CreateView):
    form_class=Reviewform
    model=Review
    success_url=reverse_lazy("chome") 
    def form_valid(self, form):
        form.instance.product=Product.objects.get(id=self.kwargs.get('pid'))
        form.instance.user=self.request.user

        return super().form_valid(form) 
    
def search_results(request):
    query = request.GET.get('q')
    results = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    context = {'query': query, 'results': results}
    return render(request, 'search.html', context)