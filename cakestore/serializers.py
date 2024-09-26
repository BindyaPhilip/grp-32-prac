# serializers.py

from django import forms
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class RegisterUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}), validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password1'])
        user.save()
        return user
