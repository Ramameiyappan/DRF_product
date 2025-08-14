from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib import messages
from . import models
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class ProductView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return render(request,'product_search.html')
    
    def post(self,request):
        productname = request.POST.get("product_name")
        return redirect('productdetail',productname=productname)
        
class ProductDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,productname):
        try:
            productdetail = models.Product.objects.get(name=productname)
            productdetail = ProductSerializer(productdetail)
            return render(request,'product_show.html',{'data':productdetail})
        except:
            messages.error(request,'The entered product is not available')
            return redirect('product')
     
    def post(self,request,productname):
        choice = request.POST.get("action")
        if choice == "Add to Cart":
            return redirect('addcart',productname=productname)
        elif choice == 'Order History':
            return redirect('showcart',user=request.user.username)
        else:
            return redirect("product")
         
class AddProduct(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request):
        return render(request,'addproduct.html')
    
    def post(self,request):
        product = ProductSerializer(data=request.POST)
        if product.is_valid():
            product.save()
            return redirect('product')
        else:
            messages.error(request,'unable to add')
            return redirect('addproduct')