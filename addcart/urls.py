from django.urls import path
from .views import AddCart,Show,OrderHistory

urlpatterns = [
    path('<str:productname>/',AddCart.as_view(),name='addcart'),
    path('show/<str:user>',Show.as_view(),name='showcart'),
    path('orderhistory',OrderHistory.as_view(),name='orderhistory')
]