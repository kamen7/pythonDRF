import graphene
from graphene_django import DjangoObjectType

from users.models import CustomUser, Photos


class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'status', 'photos', 'followed']


class PhotosType(DjangoObjectType):
    class Meta:
        model = Photos
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(CustomUserType)
    users_by_name = graphene.Field(CustomUserType, username=graphene.String(required=True))

    def resolve_all_users(root, info):
        return CustomUser.objects.all()

    def resolve_users_by_name(root, info, username):
        try:
            return CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return None
