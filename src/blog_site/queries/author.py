import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from blog_site.types.author import AuthorType


class Query(graphene.ObjectType):
    author = relay.Node.Field(AuthorType)
    authors = DjangoFilterConnectionField(AuthorType)
