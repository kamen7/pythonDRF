from rest_framework import routers

from profiles.views import ProfilesViewSet, ProfileStatusViewSet, PhotoViewSet

router = routers.DefaultRouter()
router.register(r'profile/photo', PhotoViewSet)
router.register(r'profile/status', ProfileStatusViewSet)
router.register(r'profile', ProfilesViewSet)

