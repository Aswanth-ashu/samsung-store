from django.urls import path
from .views import *
from . import views

urlpatterns=[
    path("custhome",CustHome.as_view(),name="chome"),
    path('product_details/<int:pid>',views.ProductDetails.as_view(),name="product_details"),
    path("cart",CartView.as_view(),name="cart"),
    path("checkout",CheckView.as_view(),name="c_out"),
    path("order",OrderPro.as_view(),name="order"),
    path("addcart/<int:pid>",AddCart.as_view(),name="addcart"),
    path('deletecart/<int:pid>',DeleteCart.as_view(),name="deletecart"),
    path('add_review/<int:pid>',Add_review.as_view(),name="cadd_review"),
    path('search/', views.search_results, name='search_results'),
    
]