from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,View,UpdateView,DeleteView
from .forms import ProductForm
from django.contrib import messages
from customer.models import Product

# Create your views here.





class StoreHome(CreateView):
    form_class = ProductForm
    model=Product
    template_name="shome.html"
    success_url=reverse_lazy('viewpro')
    def form_valid(self, form):
        form.instance.user=self.request.user
        self.object=form.save()
        messages.success(self.request,"Product added!")
        return super().form_valid(form)
  

class ViewPro(TemplateView):
    template_name="sview.html"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["data"]=Product.objects.filter(user=self.request.user)
        return context
    
class ProDelete(DeleteView):
    model=Product
    success_url=reverse_lazy("viewpro")
    template_name="delpro.html"
    
   
        
    
class EditPro(UpdateView):
    form_class=ProductForm
    model=Product
    success_url=reverse_lazy("viewpro")
    template_name="editpro.html"
    pk_url_kwargs="pk"
    def form_valid(self,form):
        messages.success(self.request,"Product Updated")
        self.object=form.save()
        return super().form_valid(form)    

def post(self,req,*args,**kwargs):
    d_id=kwargs.get('id')
    dept=Product.objects.get(id=d_id)
    form_data=ProductForm(req.POST,instance=dept)
    if form_data.is_valid():
        form_data.save()
        return redirect('viewpro')
    else:
        messages.error(req,"failed")
        return redirect('editpro')
