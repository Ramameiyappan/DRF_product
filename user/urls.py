from django.urls import path,include
from .views import LoginView,RegisterView,HomeView,LogoutView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout',LogoutView.as_view(),name='logout'),
    path('product/',include('product.urls'))
]