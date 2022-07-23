from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (Category, Product, ProductType, User,Profile,)

# Register your models here.

class UserAdminConfig(UserAdmin):
    ordering = ('email',)
    search_fields = ('email','username',)
    list_display = ('email','username','is_active','is_staff',)
    list_filter = ('email','username','is_active',)

    fieldsets = (
        (None,{'fields':('email','username',)}),
        ('permissions',{'fields':('is_staff','is_active',)}),
    )

    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','username','password1','password2','is_active','is_staff',),
        }),
    )


admin.site.register(User,UserAdminConfig)
admin.site.register(Profile)

admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(Category)