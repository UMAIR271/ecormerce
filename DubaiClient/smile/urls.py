"""smileface1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='ShopHome'),

    path('dashboard', views.dashboard, name='dashboard'),
    path('pricingplan', views.pricingplan, name='pricingplan'),
    path('chargestripe5doller', views.chargestripe5doller,
         name='chargestripe5doller'),
    path('chargestripe10doller', views.chargestripe10doller,
         name='chargestripe10doller'),
    path('chargestripe15doller', views.chargestripe15doller,
         name='chargestripe15doller'),
    path('submitSmile', views.submitSmile, name='submitSmile'),
    path('approve/<str:username>/', views.approve, name='approve'),
    path('disapprove/<str:username>/', views.disapprove, name='disapprove'),
    path('productdisplay', views.productdisplay, name='productdisplay'),
    path('editproduct/<int:pk>/', views.editproduct, name='editproduct'),
    path('product/<str:pk>', views.product, name='product'),
    path('checkout', views.checkout, name='checkout'),
    path('priceupdatebycategory', views.priceupdatebycategory,
         name='priceupdatebycategory'),
    path('priceupdatebycategorysubmit', views.priceupdatebycategorysubmit,
         name='priceupdatebycategorysubmit'),
    path('addNewProduct', views.addNewProduct, name='addNewProduct'),
    path('submitNewProduct', views.submitNewProduct, name='submitNewProduct'),
    path('priceupdatebyproduct', views.priceupdatebyproduct,
         name='priceupdatebyproduct'),
    path('priceupdatebyproductsubmit', views.priceupdatebyproductsubmit,
         name='priceupdatebyproductsubmit'),
    path('resetpricesforalluser', views.resetpricesforalluser,
         name='resetpricesforalluser'),
    path('view_order', views.view_order, name='view_order'),
    path('view_Category', views.view_Category, name='view_Category'),
    path('PCategory', views.PCategory, name='PCategory'),
    path('add_Category', views.add_Category, name='add_Category'),
    path('PPB_customer', views.PPB_customer, name='PPB_customer'),
    path('update_price/<int:pk>/', views.update_price,
         name='update_price'),
    path('update_price_cus', views.update_price_cus,
         name='update_price_cus'),
    path('addnewuser', views.addnewuser,
         name='addnewuser'),
    path('createnewuser', views.createnewuser,
         name='createnewuser'),
    path('productupdate', views.productupdate,
         name='productupdate'),
    path('updatecatagory', views.updatecatagory,
         name='updatecatagory'),
    path('UPB_customer', views.UPB_customer,
         name='UPB_customer'),
    path('showProduct/<str:pk>', views.showProduct, name='showProduct'),
    path('priceupdatebycategoryandusersubmit', views.priceupdatebycategoryandusersubmit, name='priceupdatebycategoryandusersubmit'),


]
