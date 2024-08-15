from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Doctor, Patient, Medication, Procedure

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Doctor
        fields = ['user', 'birth_date', 'phone_number']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['doctor', 'last_name', 'first_name', 'middle_name', 'phone_number', 'comment']

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ['doctor', 'name', 'quantity']

class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = ['doctor', 'date', 'name', 'patient']
