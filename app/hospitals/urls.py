from rest_framework import routers
from hospitals.views import HospitalViewSet
from hospitals.views import DepartmentViewSet
from hospitals.views import CostCenterViewSet

router = routers.SimpleRouter()
router.register(r'hospitals', HospitalViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'cost-centers', CostCenterViewSet)

urlpatterns = router.urls
