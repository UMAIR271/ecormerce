from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.


class Smile (models.Model):
    smileID = models.AutoField
    smileReason = models.CharField(max_length=200)
    smile_Aprroval = models.BooleanField(default=False)
    smileUserName = models.CharField(max_length=100, default="")
    smileImage = models.ImageField(upload_to='smile/images', default="")

    def __str__(self):
        return self.smileUserName


class Category(models.Model):
    cID = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    cName = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.cName


class Location(models.Model):
    lID = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    lName = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.lName


class CustomUser(AbstractUser):

    prID = models.AutoField(primary_key=True)
    prPricingRuleName = models.CharField(max_length=300)
    prPrcingtwo = models.CharField(max_length=300, default="")
    pricing3 = models.CharField(max_length=300, default="")
    pLoc = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True)


class Product(models.Model):
    Id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    pHandle = models.AutoField
    pName = models.CharField(max_length=250, unique=True)
    pDescription = models.CharField(max_length=250, default="")
    pCategories = models.ForeignKey(
        Category, on_delete=models.SET_DEFAULT, default=1)
    pPrice = models.IntegerField(default=0)
    pQTY = models.IntegerField(default=0)

    def __str__(self):
        return self.pName


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
    OrderDetails = models.CharField(max_length=5000, default="")


class PricingRule(models.Model):
    prID = models.AutoField(primary_key=True)
    prPricingRuleName = models.CharField(
        max_length=300, default="", unique=True)
    pIncreaseFix = models.IntegerField()
    pIncreasebyPercentage = models.IntegerField()

    def __str__(self):
        return self.prPricingRuleName


class ProductPricingList(models.Model):

    pplID = models.AutoField(primary_key=True)

    pMarkup = models.IntegerField(default=1)
    cMarkup = models.IntegerField(default=1)
    lMarkup = models.IntegerField(default=1)
    pName = models.CharField(max_length=220, default="")
    pID = models.ForeignKey(
        Product, on_delete=models.SET_DEFAULT, default=1)
    cID = models.ForeignKey(
        Category, on_delete=models.SET_DEFAULT, default=1)
    lID = models.ForeignKey(
        Location, on_delete=models.SET_DEFAULT, default=1)
    uID = models.ForeignKey(
        CustomUser, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.pName
