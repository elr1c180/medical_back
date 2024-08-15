# serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Doctor, Medication

User = get_user_model()

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['user', 'birth_date', 'phone_number']

class RegisterDoctorSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    birth_date = serializers.DateField()
    phone_number = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'birth_date', 'phone_number']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        Doctor.objects.create(
            user=user,
            birth_date=validated_data['birth_date'],
            phone_number=validated_data['phone_number']
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        print(email, password)
        if email and password:
            user = authenticate(email=email, password=password)

            if not user:
                raise serializers.ValidationError('Invalid credentials')
            return {
                'user': user,
                'access': str(RefreshToken.for_user(user).access_token),
                'refresh': str(RefreshToken.for_user(user))
            }
        raise serializers.ValidationError('Both email and password are required')

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ['id', 'name', 'quantity']
