from dataclasses import field
from rest_framework import serializers
from hospitals.models import Hospital
from hospitals.models import Department
from hospitals.models import Cost_Center



class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class CostCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cost_Center
        fields = '__all__'
