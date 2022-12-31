import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from blog_site.models.post import Post


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        filter_fields = {
            "id": ["exact"],
            "title": ["exact", "icontains", "istartswith"],
            "content": ["icontains", "istartswith"],
            "author__id": ["exact"],
            "author__name": ["exact", "icontains", "istartswith"],
        }
        interfaces = (relay.Node,)
