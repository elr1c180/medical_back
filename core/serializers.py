from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Doctor, Medication

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class DoctorSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField()
    phone_number = serializers.CharField()

    class Meta:
        model = Doctor
        fields = ['birth_date', 'phone_number']

class RegisterDoctorSerializer(serializers.Serializer):
    user = UserSerializer()
    doctor = DoctorSerializer()

    def create(self, validated_data):
        user_data = validated_data['user']
        doctor_data = validated_data['doctor']
        
        # Создание пользователя
        user = User.objects.create_user(**user_data)
        
        # Создание профиля врача
        Doctor.objects.create(user=user, **doctor_data)
        
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
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
