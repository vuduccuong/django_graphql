import graphene
from graphene import relay
from graphene_django import DjangoObjectType, DjangoListField

from blog_site.models.author import Author
from blog_site.models.post import Post
from blog_site.types.post import PostType


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        filter_fields = {
            "id": ["exact"],
            "name": ["exact", "icontains", "istartswith"],
        }
        interfaces = (relay.Node,)

    posts = DjangoListField(PostType)

    def resolve_posts(self, info):
        return Post.objects.filter(author=self)
