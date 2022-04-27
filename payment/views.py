from django.shortcuts import redirect, render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response 
from rest_framework import status 
import stripe 
from django.conf import settings
from .models import Price 


stripe.api_key = settings.STRIPE_SECRET_KEY 

@api_view(['GET'])
def get_routes(request):
    if request.method == 'GET':
        routes = {
            "checkout-session": "/payment/checkout-session",
            "payment-success": "/payment/success",
            "payment-cancel": "/payment/cancel",
        }

        return Response(routes, status=status.HTTP_200_OK)
    else:
        return Response({"Error": "Invalid request type"})

@api_view(['POST'])
def checkout_session_view(request, id):
    if request.method == 'POST':
        price = Price.objects.get(plan=id)
        your_domain = "https://127.0.0.1:8000/payment"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                }
            ], 
            mode='payment',
            success_url = f"{your_domain}/sucess/",
            cancel_url= f"{your_domain}/cancel/",
        )

        return redirect(checkout_session.url)

    else:
        return Response({"Error": "Invalid request type"})
        

@api_view(['GET'])
def success_url(request):
    if request.method == "GET":
        return Response({"Success": "Your purchase was a success"})
    else:
        return Response({"Error": "Invalid request type"})

@api_view(['GET'])
def cancel_url(request):
    if request.method == "GET":
        return Response({"Not Successfull": "Your purchase was not successful"})
    else:
        return Response({"Error": "Invalid request type"})