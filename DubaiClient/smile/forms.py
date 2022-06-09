from math import prod
from statistics import mode
from tkinter import Widget
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Smile, Product, CustomUser, Category


class smileSubmitForm (ModelForm):
    class Meta:
        model = Smile
        fields = '__all__'
        widgets = {
            'smileReason': forms.TextInput(attrs={'class': 'form-control'}),
            'smileUserName': forms.TextInput(attrs={'class': 'form-control'}),
        }


class formProduct (ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CustomUserForm (UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'pLoc')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),

        }

    def customsave(self, user):
        lv = self.save(commit=False)
        lv.created_by = user
        lv.save()
        return lv


class addNewProductform (ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class addNewcatgory (ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
