from rest_framework import routers

from posts.views import PostsViewSet
from api.router import router

router.register(r'posts', PostsViewSet)


