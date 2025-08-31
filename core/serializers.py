from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Patient, Doctor, Mapping

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id','name','username','email','password')

    def create(self, validated_data):
        name = validated_data.pop('name', '')
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = name
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name','email')

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Patient
        fields = '__all__'

class MappingSerializer(serializers.ModelSerializer):
    assigned_by = UserSerializer(read_only=True)
    class Meta:
        model = Mapping
        fields = '__all__'
