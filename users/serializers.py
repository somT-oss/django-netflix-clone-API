from .models import User
from rest_framework import serializers

class UsereRegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User 
        fields = [
            "id",
            "username",
            "email",
            "password"
        ]

    def validate(self, attrs):
        email = attrs.get("email", "")
        username = attrs.get("username", "")
        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user