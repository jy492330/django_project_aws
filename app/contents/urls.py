from rest_framework import routers
from contents.views import HostedContentViewSet
from contents.views import UploadedContentViewSet
from contents.views import CheckedContentViewSet

router = routers.SimpleRouter()
router.register(r'hosted-contents', HostedContentViewSet)
router.register(r'uploaded-contents', UploadedContentViewSet)
router.register(r'checked-out-contents', CheckedContentViewSet)

urlpatterns = router.urls
