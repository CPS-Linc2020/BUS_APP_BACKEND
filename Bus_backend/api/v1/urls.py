from rest_framework.routers import DefaultRouter

from Bus_backend.api.v1.views import BusApiViewSet

router = DefaultRouter()
router.register(r'bus', BusApiViewSet, basename='bus')
urlpatterns = router.urls
