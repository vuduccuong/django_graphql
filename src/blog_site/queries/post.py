import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from blog_site.types.post import PostType


class Query(graphene.ObjectType):
    post = relay.Node.Field(PostType)
    posts = DjangoFilterConnectionField(PostType)
