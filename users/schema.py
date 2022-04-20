import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q

from users.models import CustomUser, Photos


class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'status', 'photos', 'followed', 'first_name', 'last_name']


class PhotosType(DjangoObjectType):
    class Meta:
        model = Photos
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(CustomUserType)
    find_user = graphene.List(CustomUserType,
                              findBy=graphene.String(required=True),
                              offset=graphene.Int(required=False),
                              limit=graphene.Int(required=False))

    def resolve_all_users(self, info):
        return CustomUser.objects.all()

    def resolve_find_user(self, info, findBy, offset=None, limit=None):
        qs = CustomUser.objects.filter(Q(username=findBy) | Q(first_name=findBy) | Q(last_name=findBy) |
                                       Q(email=findBy) | Q(status=findBy))
        if offset:
            qs = qs[offset:]

        if limit:
            qs = qs[:limit]

        return qs
