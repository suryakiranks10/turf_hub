from django.contrib.auth.models import User

from rest_framework import serializers

class AdminSerializer(serializers.Serializer):

    username = serializers.CharField()

    email = serializers.CharField()

    password = serializers.CharField()


    def create(self, validated_data):
        
        return User.objects.create_superuser(**validated_data)

class UserSerializer(AdminSerializer):

    def create(self, validated_data):
        
        return User.objects.create_user(**validated_data)