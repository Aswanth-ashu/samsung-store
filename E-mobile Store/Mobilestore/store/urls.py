from django.urls import path
from .views import StoreHome,ViewPro,ProDelete,EditPro

urlpatterns=[
    path("storeh",StoreHome.as_view(),name="shome"),
    path("store",StoreHome.as_view(),name="store"),
    path("viewpro",ViewPro.as_view(),name="viewpro"),
    path('prodel/<int:pk>',ProDelete.as_view(),name='prodel'),
    path('editpro/<int:pk>',EditPro.as_view(),name='editpro')

]