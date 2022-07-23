from rest_framework import viewsets,generics,mixins
from .models import (
    User,
    Profile,
    Product,
    ProductType,
    Category
    )
from .serializer import (
    ProfileSerializer,
    UserSerializer,
    ProductSerializer,
    ProductTypeSerializer,
    CategorySerializer
    )

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductTypeViewset(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

