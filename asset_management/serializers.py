from rest_framework import serializers
from .models import Company, Device, CheckOut

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class CheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckOut
        fields = '__all__'
