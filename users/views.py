from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import CustomUser
from users.serializers import UserSerializer
from users.serializers import StatusSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        users = CustomUser.objects.all()

        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response(data=serializer.data)
