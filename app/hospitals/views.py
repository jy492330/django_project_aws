from rest_framework import viewsets

from hospitals.models import (
    Hospital,
    Department,
    Cost_Center
)
from hospitals.serializers import (
    HospitalSerializer,
    DepartmentSerializer,
    CostCenterSerializer
)


class HospitalViewSet(viewsets.ModelViewSet):
    serializer_class = HospitalSerializer
    queryset = Hospital.objects.all()


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class CostCenterViewSet(viewsets.ModelViewSet):
    serializer_class = CostCenterSerializer
    queryset = Cost_Center.objects.all()
