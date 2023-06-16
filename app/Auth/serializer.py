from rest_framework import serializers
from . import models

class UserModelSerializer(serializers.ModelSerializer):
    """Serializer for User objects"""

    class Meta:
        model = models.UserModel
        fields = ('id', 'username', 'email', 'name', 'dob', 'dob', 'gender', 'country', 'state', 'city', 'pincode', 'password', 'is_active', 'is_premium_user')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserModel.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            name=validated_data['name'],
            dob=validated_data['dob'],
            gender=validated_data['gender'],
            country=validated_data['country'],
            state=validated_data['state'],
            city=validated_data['city'],
            pincode=validated_data['pincode'],
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

class DiaryModelSerializer(serializers.ModelSerializer):
    """Serializer for Diary models"""

    class Meta:
        model = models.DiaryModel
        unique_together = ('author', 'date')
        fields = ('id', 'author', 'date', 'description')
        extra_kwargs = {
            'author': {'read_only': True},
            'date': { 'read_only': True}
        }