from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import CustomUser, Photos
from users.serializers import StatusSerializer
from profiles.models import Profile, Contacts
from profiles.serializers import ProfileSerializer, ContactsSerializer, PhotoSerializer


class ProfilesViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(data=serializer.data)

    def create(self, request, *args, **kwargs):
        profiles = Profile.objects.filter(user=self.request.user)
        serializer = ContactsSerializer(data=request.data)
        print(request.user)
        serializer.is_valid(raise_exception=True)

        return Response(status=status.HTTP_200_OK)


class ProfileStatusViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = StatusSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.status = serializer.data['status']
        request.user.save()

        return Response(status=status.HTTP_200_OK)


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photos.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = PhotoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.photos = serializer.data
        request.user.save()

        return Response(status=status.HTTP_200_OK)
