from django.shortcuts import render,redirect
from rest_framework.views import APIView
from .models import Cart
from product.models import Product
from product.serializers import ProductSerializer
from .serializers import CartSerializer
from django.contrib import messages
from rest_framework.permissions import IsAuthenticated,IsAdminUser


class AddCart(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,productname):
        return self.post(request,productname)

    def post(self,request,productname):
        username = request.user.username
        if not username:
            messages.error(request, "Please login to add products to your cart.")
            return redirect('login')
        try:
            productdetail = Product.objects.get(name=productname)
        except:
            messages.error(request,'product is not available')
            return redirect('product')
        if productdetail.stock <= 0:
            messages.error(request,"product sold out")
            return redirect('product')
        productdetail = Product.objects.get(name=productname)
        productdetail.sold += 1
        productdetail.stock -= 1
        data = {
            'product':productname,
            'customer' : username,
        }
        dataserial = CartSerializer(data=data)
        if dataserial.is_valid():
            dataserial.save()
            productdetail.save()
            return redirect('showcart',user=username)
        else:
            messages.error(request, "Unable to add to cart.")
            return redirect('product')
    
class Show(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,user):
        form = Cart.objects.filter(customer=user)
        formserial = CartSerializer(form,many=True)
        return render(request,'show.html',{'data':formserial.data})
    
    def post(self, request, user):
        action = request.POST.get("action")
        cart_id = request.POST.get("cart_id")

        if action == "Delete" and cart_id:
            try:
                cart_item = Cart.objects.get(id=cart_id, customer=request.user.username)
                product_data = Product.objects.get(name=cart_item.product)
                product_data.sold -= 1
                product_data.stock += 1
                product_data.save()
                cart_item.delete()
                messages.success(request, "Item deleted successfully.")
            except (Cart.DoesNotExist, Product.DoesNotExist):
                messages.error(request, "Item not found or cannot be deleted.")
        return self.get(request,user)
        
class OrderHistory(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request):
        data = Cart.objects.all()
        dataserial = CartSerializer(data,many=True)
        return render(request,'order.html',{'data':dataserial.data})
    def post(self, request):
        action = request.POST.get("action")
        cart_id = request.POST.get("cart_id")

        if action == "Delete" and cart_id:
            try:
                cart_item = Cart.objects.get(id=cart_id)
                product_data = Product.objects.get(name=cart_item.product)
                product_data.sold -= 1
                product_data.stock += 1
                product_data.save()
                cart_item.delete()
                messages.success(request, "Item deleted successfully.")
            except (Cart.DoesNotExist, Product.DoesNotExist):
                messages.error(request, "Item not found or cannot be deleted.")
        return self.get(request)