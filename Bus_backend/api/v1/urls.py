from rest_framework.routers import DefaultRouter

from .views import BusApiViewSet

router = DefaultRouter()
router.register(r'bus', BusApiViewSet, basename='bus')
urlpatterns = router.urls
