from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Medication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import RegisterDoctorSerializer, LoginSerializer, MedicationSerializer

@api_view(['POST'])
def register_doctor(request):
    serializer = RegisterDoctorSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            'user': serializer.data,
            'access': str(RefreshToken.for_user(user).access_token),
            'refresh': str(RefreshToken.for_user(user))
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_doctor(request):
    serializer = LoginSerializer(data=request.data)
    print(serializer)
    print(request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        return Response({
            'access': data['access'],
            'refresh': data['refresh']
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MedicationListView(generics.ListAPIView):
    serializer_class = MedicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Получаем текущего пользователя
        user = self.request.user
        # Возвращаем все препараты, связанные с врачом текущего пользователя
        return Medication.objects.filter(doctor__user=user)