from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Patient, Doctor, Mapping
from .serializers import RegisterSerializer, PatientSerializer, DoctorSerializer, MappingSerializer

class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = []

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]


class MappingCreateListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        mappings = Mapping.objects.all()
        serializer = MappingSerializer(mappings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(assigned_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
