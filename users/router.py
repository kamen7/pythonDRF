from rest_framework import routers
from users.views import UserViewSet, StatusViewSet

router = routers.DefaultRouter()
router.register(r'users/status', StatusViewSet)
router.register(r'users', UserViewSet)

