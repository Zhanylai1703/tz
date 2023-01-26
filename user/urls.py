from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet


router = DefaultRouter()
router.register('user', CustomUserViewSet, basename='user')

urlpatterns = router.urls