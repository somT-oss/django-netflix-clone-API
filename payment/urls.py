from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.get_routes, name='payment-routes'),
    path('checkout-payment/', views.checkout_session_view, name='checkout-payment'),
    path('payment-success/', views.success_url, name='payment-success'),
    path('payment-cancel/', views.cancel_url, name='payment-cancel')
]