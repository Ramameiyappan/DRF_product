from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import AllowAny

class HomeView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        return render(request,'home.html')
    
    def post(self,request):
        choice = request.POST.get('login')
        if choice == 'login':
            return redirect('login')
        else:
            return redirect('register')
        
class LoginView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        return render(request,'login.html')
    
    def post(self,request):
        user = request.POST.get('username')
        pass_ = request.POST.get('password')
        if not User.objects.filter(username=user).exists():
            messages.error(request, 'User not registered. Please register first.')
            return redirect('register')
            
        userdetail = authenticate(request, username=user, password=pass_)
        if userdetail is not None:
            login(request, userdetail)
            return redirect('product')
        else:
            messages.error(request,'Password mismatch')
            return render(request,"login.html")        
        
class RegisterView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        return render(request,'register.html')
    
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')
        User.objects.create_user(username=username, password=password)
        messages.error(request, 'User registered successfully. Please login.')
        return redirect('login')
        
class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return redirect('home')
    
