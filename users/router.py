from rest_framework import routers
from users.views import UserViewSet, StatusViewSet
from api.router import router

router.register(r'users/status', StatusViewSet)
router.register(r'users', UserViewSet)

