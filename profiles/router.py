from rest_framework import routers

from profiles.views import ProfilesViewSet, ProfileStatusViewSet, PhotoViewSet
from api.router import router

router.register(r'profile/photo', PhotoViewSet)
router.register(r'profile/status', ProfileStatusViewSet)
router.register(r'profile', ProfilesViewSet)

