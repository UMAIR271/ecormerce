from distutils.command.build_scripts import first_line_re
import imp
from django.contrib import admin
from .forms import CustomUserForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Smile, Product, Category, Orders, CustomUser, PricingRule, ProductPricingList, Location


class CustomerUserAdmin (UserAdmin):

    model = CustomUser
    add_form: CustomUserForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User role',
            {
                'fields': (


                    'pLoc',
                    'prPrcingtwo'
                )
            }


        )
    )


admin.site.register(Smile)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Orders)
admin.site.register(CustomUser, CustomerUserAdmin)
admin.site.register(PricingRule)
admin.site.register(ProductPricingList)
admin.site.register(Location)
