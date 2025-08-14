from django.urls import path,include
from .views import ProductView,ProductDetail,AddProduct

urlpatterns = [
    path('',ProductView.as_view(),name='product'),
    path('addcart/',include('addcart.urls')),
    path('addproduct/',AddProduct.as_view(),name='addproduct'),
    path('<str:productname>/',ProductDetail.as_view(),name='productdetail'),
]