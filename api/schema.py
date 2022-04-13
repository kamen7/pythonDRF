import graphene
from users.schema import Query as UsersQuery
from profiles.schema import Query as ProfilesQuery
from posts.schema import Query as PostQuery
from follows.schema import Query as FollowQuery


class Query(FollowQuery, PostQuery, ProfilesQuery, UsersQuery, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


schema = graphene.Schema(query=Query)
