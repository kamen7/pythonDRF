from rest_framework import routers

from follows.views import FollowViewSet
from api.router import router

router.register(r'follows', FollowViewSet)
