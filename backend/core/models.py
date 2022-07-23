from distutils.command.upload import upload
from email.policy import default
from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
    )

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_superuser(self,email,username,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        return self.create_user(email,username,password,**other_fields)
    
    def create_user(self,email,username,password,**other_fields):
        if not email:
            raise ValueError(_('please provide an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email,username=username,**other_fields)

        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser,PermissionsMixin):
    email       = models.EmailField(_('email address'),unique=True)
    username    = models.CharField(max_length=20,unique=True)
    is_staff    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username']

class Profile(models.Model):
    user            = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    middle_name     = models.CharField(max_length=20,blank=True,null=True)
    profile_pics    = models.ImageField(upload_to='profile_pics',default='profile.png')

    def __str__(self):
        return f'{self.user}'

class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.category}'

class ProductType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.type}'

class Product(models.Model):
    product_type = models.ForeignKey(ProductType,on_delete=models.CASCADE)
    product_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    feature_image = models.ImageField(upload_to='product_images',default='product_image.png')

    def __str__(self):
        return f'{self.title}'