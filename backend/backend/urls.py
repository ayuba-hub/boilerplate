from atexit import register
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from core.viewsets import (
    ProfileViewset,
    ProductViewset,
    ProductTypeViewset,
    UserViewset,
    CategoryViewset,
    )


admin.site.site_header = 'LinkMart'
admin.site.site_title = 'LinkMart'

router = routers.DefaultRouter()

router.register(r'user',UserViewset)
router.register(r'profile',ProfileViewset)
router.register(r'product',ProductViewset)
router.register(r'product_type',ProductTypeViewset)
router.register(r'category',CategoryViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    #path('api/profile/', ProfileViewset.as_view()),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
