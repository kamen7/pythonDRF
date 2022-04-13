import graphene
from graphene_django import DjangoObjectType

from posts.models import Image, Post


class ImageType(DjangoObjectType):
    class Meta:
        model = Image
        fields = '__all__'


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = '__all__'


class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)

    def resolve_all_posts(root, info):
        return Post.objects.all()

