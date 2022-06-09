from email import message
import imp
from multiprocessing import context
import re
from unicodedata import category
from django.contrib import messages
from django.core.mail import send_mail
from numpy import true_divide
from requests import post
from smileface1.settings import EMAIL_HOST_USER
import os
from django.conf import settings
from pyexpat.errors import messages
from urllib import response
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Smile, Product, Category, Orders, CustomUser, ProductPricingList, Location
import matplotlib.pyplot as plt
import json
from smileface1 import settings
from .forms import CustomUserForm, smileSubmitForm, formProduct, addNewProductform, addNewcatgory
import stripe
from django.contrib.auth import get_user_model
stripe.api_key = settings.STRIPE_SECRET_KEY


def index(request):
    # return HttpResponse("Hello")
    return render(request, 'smile/index.html')


def dashboard(request):
    if request.user.is_superuser:
        Corder = Orders.objects.all()
        context = {
            "Corder": Corder,
        }
        return render(request, 'smile/admindashboard.html', context)
    else:

        form = smileSubmitForm()
        form = smileSubmitForm(
            initial={'smileUserName': request.user.username})

        context = {'form': form}
        return render(request, 'smile/dashboard.html', context)


def productdisplay(request):
    if request.user.is_superuser:
        productdata = Product.objects.all()

        processProducts = True
        context = {
            "productdata": productdata,
        }
        return render(request, 'smile/admindashboard.html', context)

    else:
        return HttpResponse("Hello Motto")


def submitSmile(request):
    if request.method == 'POST':
        request.FILES['smileImage'].name = request.user.username + '.png'
        form = smileSubmitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('pricingplan')


def pricingplan(request):
    my_context = {
        "key": settings.STRIPE_PUBLISHABLE_KEY
    }
    return render(request, 'smile/pricingplan.html', my_context)


def chargestripe5doller(request):
    if request.method == 'POST':

        try:
            charge = stripe.Charge.create(
                amount=500,
                currency='usd',
                description='Payment Gateway',
                source=request.POST['stripeToken']
            )
        except stripe.error.CardError as e:
            # Problem with the card
            pass
        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            pass
        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe API
            pass
        except stripe.error.AuthenticationError as e:
            # Authentication Error: Authentication with Stripe API failed (maybe you changed API keys recently)
            pass
        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            pass
        except stripe.error.StripeError as e:
            # Stripe Error
            pass
        else:
            # success
            return render(request, 'charge.html')


def chargestripe10doller(request):
    if request.method == 'POST':

        try:
            charge = stripe.Charge.create(
                amount=1000,
                currency='usd',
                description='Payment Gateway',
                source=request.POST['stripeToken']
            )
        except stripe.error.CardError as e:
            # Problem with the card
            pass
        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            pass
        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe API
            pass
        except stripe.error.AuthenticationError as e:
            # Authentication Error: Authentication with Stripe API failed (maybe you changed API keys recently)
            pass
        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            pass
        except stripe.error.StripeError as e:
            # Stripe Error
            pass
        else:
            # success
            return render(request, 'charge.html')


def chargestripe15doller(request):
    if request.method == 'POST':

        try:
            charge = stripe.Charge.create(
                amount=1500,
                currency='usd',
                description='Payment Gateway',
                source=request.POST['stripeToken']
            )
        except stripe.error.CardError as e:
            # Problem with the card
            pass
        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            pass
        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe API
            pass
        except stripe.error.AuthenticationError as e:
            # Authentication Error: Authentication with Stripe API failed (maybe you changed API keys recently)
            pass
        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            pass
        except stripe.error.StripeError as e:
            # Stripe Error
            pass
        else:
            # success
            return render(request, 'charge.html')


def approve(request, username):
    var1 = Smile.objects.filter(
        smileUserName=username).update(smile_Aprroval=True)
    if var1:
        approval_user = Smile.objects.get(smileUserName=username)
        approval_image = approval_user.smileImage
        plt.savefig(os.path.join(settings.BASE_DIR, f"{approval_image}"))
        print("umair")
    else:
        pass

    return render(request, 'charge.html')


def disapprove(request, username):
    query = username
    var1 = Smile.objects.filter(
        smileUserName=query).update(smile_Aprroval=False)
    to_send = User.objects.all()
    usera = User.objects.get(username=username)
    useremail = usera.email
    print(useremail)
    message = "your image not Approved plaese wait"
    from_email = EMAIL_HOST_USER
    to_recipent = [useremail, 'usmankhankh321@gmail.com']
    send_mail(
        username,
        message,
        from_email,
        to_recipent,
        fail_silently=False,
    )
    return render(request, 'charge.html')


def editproduct(request, pk):

    if request.user.is_superuser:
        form = formProduct()

        context = {'form': form}
        return render(request, 'smile/editproduct.html', context)


def product(request, pk):

    product = Product.objects.filter(Id=pk)

    context = {'product': product}
    return render(request, 'smile/product.html', context)


def checkout(request):
    my_context = {
        "key": settings.STRIPE_PUBLISHABLE_KEY
    }
    if request.method == "POST":

        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        print(items_json)
        dictData = json.loads(items_json)
        ProductDetails = ""
        for product in dictData:
            print(product)
            ProductDetails1 = "Product Name : " + \
                dictData[product][1].strip() + "  " + "Product Qty " + \
                str(dictData[product][0]) + " Product Price " + \
                str(dictData[product][2]) + "\n"
            ProductDetails = ProductDetails + ProductDetails1

        print(ProductDetails)

        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + \
            " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone, OrderDetails=ProductDetails)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'smile/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'smile/checkout.html')


def priceupdatebycategory(request):
    category = Category.objects.all()
    category1=Category.objects.values()
    print(category1)
    print(type(category1))
    context = {
        'categorys':category,
        'category1':category1
    }
    return render(request, 'smile/admindashboard.html', context)


def priceupdatebycategorysubmit(request):
    key = request.POST["key"]
    CategoryMarkup = request.POST["CategoryMarkup"]
    data = ProductPricingList.objects.filter(cID=key)
    print(data)
    for entry in data:
        ProductPricingList.objects.filter(pplID=entry.pplID).update(cMarkup=CategoryMarkup) 
    return HttpResponse('Ok')

def priceupdatebycategoryandusersubmit(request):
    CategoryNAME = request.POST["CategoryNAME"]
    UserName = request.POST["UserName"]
    CategoryMarkup = request.POST["CategoryMarkup"]
    user=CustomUser.objects.filter(username = UserName).values()
    print(user,"user_value")
    cid = Category.objects.filter(cName = CategoryNAME).values()
    print(cid)
    data = ProductPricingList.objects.filter(cID=cid, uID = user)
    print(data)

    for entry in data:
           ProductPricingList.objects.filter(pplID=entry.pplID).update(cMarkup=CategoryMarkup) 
    return HttpResponse('Ok')

def priceupdatebyproduct(request):

    return render(request, 'smile/priceupdatebyproduct.html')


def priceupdatebyproductsubmit(request):

    username = request.POST["username"]
    productname = request.POST["productname"]
    print(username, productname)
    updatepricebypercent = request.POST["updatepricebypercent"]

    data = ProductPricingList.objects.filter(
        username=username, productname=productname).values_list('pplID', 'username', 'productname', 'productPrice')
    print(data)
    for products in data:
        print(products[0])
        updatedPriceis = products[3] + int(updatepricebypercent)

        ProductPricingList.objects.filter(
            pplID=products[0]).update(productPrice=updatedPriceis)

    return HttpResponse('Updated')


def addNewProduct(request):

    form = addNewProductform()

    context = {'form': form}
    return render(request, 'smile/addNewProduct.html', context)


def submitNewProduct(request):
    pName = ""
    cId = ""
    pPrice = ""
    lId = ""
    pId = ""
    if request.method == 'POST':
        form = addNewProductform(request.POST, request.FILES)
        if form.is_valid():
            pName = form.cleaned_data.get("pName")
            cId = form.cleaned_data.get("pCategories")
            lId = form.cleaned_data.get("pLoc")
            pPrice = form.cleaned_data.get("pPrice")

            pId = form.save()

    User = get_user_model()
    users = User.objects.all()

    for username in users:

        locobjtmodel = Location.objects.filter(lName=username.pLoc)
        for lId in locobjtmodel:

            productPricingList = ProductPricingList(pID=pId, uID=username,
                                                    cID=cId, lID=lId,  pName=pName)
            productPricingList.save()

    return HttpResponse('Product Added')


def resetpricesforalluser(request):

    User = get_user_model()
    users = User.objects.all()
    allProducts = Product.objects.values()

    for username in users:
        print(username)
        for products in allProducts:

            productupdate = ProductPricingList.objects.filter(
                username=username, productname=products['pName']).update(productPrice=products['pPrice'])

    return HttpResponse("Hello Motto")


def view_order(request):
    print("umair")
    if request.user.is_superuser:
        Corder = Orders.objects.all()
        context = {
            "Corder": Corder,
        }
        return render(request, 'smile/admindashboard.html', context)
    else:
        return HttpResponse("Hello Motto")


def view_Category(request):
        C_Category = Category.objects.all()
        print(C_Category)
        context = {
            "C_Category": C_Category,
        }
        return render(request, 'smile/admindashboard.html', context)


def PCategory(request):
    form = addNewcatgory()
    context = {
        'form': form
    }
    return render(request, 'smile/addnewcategory.html', context)


def add_Category(request):
    print("umairs")
    if request.method == "POST":
        cName = request.POST.get('cName')
        add_Category = Category(cName=cName)
        add_Category.save()

        return render(request, 'smile/admindashboard.html',)
    else:
        return HttpResponse("Hello Motto")


def PPB_customer(request):

    if request.method == "POST":
        productPriceCustomer = request.POST.get('productPriceCustomer', None)

        users = CustomUser.objects.all()
        userid = ""
        for user in users:
            if user.username == productPriceCustomer:
                userid = user.prID
        print(userid)
        displayproductbycustomer = ProductPricingList.objects.filter(
            uID=userid).values('pplID', 'pName', 'lMarkup', 'cMarkup', 'pMarkup')
        print(displayproductbycustomer)
        context = {
            'displayproductbycustomer': displayproductbycustomer,
            'customername': productPriceCustomer
        }

        return render(request, 'smile/admindashboard.html', context)
    else:
        return render(request, 'smile/productpricecustomer.html',)


def update_price(request, pk):
    print(pk)

    context = {
        'updateid': pk
    }
    return render(request, 'smile/priceupdate.html', context)


def update_price_cus(request):

    if request.method == "POST":
        Priceupdate = request.POST.get('Priceupdate')
        key = request.POST.get('key')

        print(Priceupdate)
        print(type(Priceupdate))

        print(key)
        print(type(key))

        finalPrice = ProductPricingList.objects.filter(
            pplID=key).update(productPrice=Priceupdate)
        print(finalPrice)
        context = {
            'productupdate': finalPrice
        }

        return HttpResponse("Hello ")


def addnewuser(request):

    form = CustomUserForm()
    context = {
        'form': form
    }
    return render(request, 'smile/addnewuserform.html', context)


def updatecatagory(request):
    if request.method == "POST":
        key = request.POST.get('key')
        CategoryNAME = request.POST.get('CategoryNAME')
        update1 = Category.objects.filter(cID=key).update(cName=CategoryNAME)
        print(update1)
        print(key,CategoryNAME)
        #
        return view_Category(request)


def productupdate(request):
    if request.method == "POST":
        key = request.POST.get('key')
        ProductNAME = request.POST.get('ProductNAME')
        ProductDescription = request.POST.get('ProductDescription')
        productPrice = request.POST.get('productPrice')
        productQunatity = request.POST.get('productQunatity')
        print(key, ProductNAME,
              productPrice,ProductDescription, productQunatity)
        product = Product.objects.filter(Id=key)
        print(product)
        product.update(pName=ProductNAME, pDescription=ProductDescription, pPrice=productPrice, pQTY=productQunatity)

        return productdisplay(request)


def UPB_customer(request):
    if request.method == "POST":
        key = request.POST.get('key')
        lMarkup = request.POST.get('lMarkup')
        cMarkup = request.POST.get('cMarkup')
        pMarkup = request.POST.get('pMarkup')
        usersearched = request.POST.get('usersearched')

        print(key, lMarkup, cMarkup, pMarkup)

        ProductPricingList.objects.filter(pplID=key).update(
            lMarkup=lMarkup, cMarkup=cMarkup, pMarkup=pMarkup)
        # return redirect(request.META['HTTP_REFERER'])
        return HttpResponse("updated")


def createnewuser(request):
    print("here")
    print(request)
    if request.method == 'POST':
        print("inhere")
        # Get Parameters
        username = request.POST["username"]
        user = username.lower()

        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        password2 = request.POST['password2']
        pLocID = request.POST['pLoc']

        pLoc = Location.objects.get(lID=pLocID)

        # Checks
        if password1 == password2:
            if password1:
                if CustomUser.objects.filter(username=user).exists():
                    messages.success(request, "this user is already exsit!")
                    return redirect('addnewuserform')
        # create user
                else:

                    print(username)

                    form = CustomUserForm(request.POST, request.FILES)
                    if form.is_valid():

                        pId = form.save()
                    User = get_user_model()
                    users = User.objects.all()
                    CreateProductUSer = ""
                    for user1 in users:
                        print("Inside For")
                        print(user1)
                        if user1.username == username:
                            CreateProductUSer = user1
                            print(type(CreateProductUSer))
                            print(CreateProductUSer)

                            products = Product.objects.all()

                            for product in products:

                                print(product.pCategories)
                                categoryobjtmodel = Category.objects.filter(
                                    cName=product.pCategories)
                                for cat in categoryobjtmodel:

                                    productPricingList = ProductPricingList(
                                        pID=product, uID=CreateProductUSer, cID=cat, lID=pLoc,  pName=product.pName)
                                    productPricingList.save()

                    print(users)
                    # print(type(newuser))
                    #print('User Saved')
                    products = Product.objects.values()
                    for products in products:
                        print('Ok')
                        # print(type(products))
                        # productupdate = ProductPricingList.objects.filter(
                        # username=username, productname=products['pName']).update(productPrice=products['pPrice'])

                    return render(request, 'index.html')
            else:

                return HttpResponse("Wrong Information")
        else:
            return HttpResponse("Pasword Wrong Information")
            # create user
    else:
        return HttpResponse('Not Allowed')

    # return HttpResponse("Hello")
    return render(request, 'index.html')
    return HttpResponse('createnewuser  ')


def showProduct(request, pk):
    category = Category.objects.all
    product = Product.objects.filter(pCategories=pk)

    print(category)
    print(type(category))
    context = {
        'category': category,
        'products': product,

    }
    return render(request, 'index.html', context)
