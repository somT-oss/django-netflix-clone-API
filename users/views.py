from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response 
from .serializers import UsereRegistrationSerializer
from .models import User

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        register_serializer = UsereRegistrationSerializer(data=request.data)
        if register_serializer.is_valid():
            db_username = User.objects.values_list('username', flat=True) 
            user_username = register_serializer.validated_data.get('username')
            if user_username in db_username:
                return Response({"Error": f"User with the username {user_username} already exists"}, status=status.HTTP_400_BAD_REQUEST)
            db_email = User.objects.values_list('email', flat=True)
            user_email = register_serializer.validated_data.get('email')
            if user_email in db_email:
                return Response({"Error": f"User with the email {user_email} already exists"}, status=status.HTTP_400_BAD_REQUEST)
            register_serializer.save()
            message  = {
                "id": register_serializer.data.get('id'),
                "username": register_serializer.data.get('username'),
                "email": register_serializer.data.get('email'),
            }
            return Response(message, status=status.HTTP_201_CREATED)
        else:
            return Response(register_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"Error": "Invalid request type"}, status=status.HTTP_400_BAD_REQUEST)