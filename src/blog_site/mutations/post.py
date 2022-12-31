import http
from datetime import datetime

import graphene
from graphene import relay
from graphql_relay import from_global_id

from blog_site.models import Post
from blog_site.types import PostType


class AddPost(relay.ClientIDMutation):
    class Input:
        title = graphene.String(required=True)
        content = graphene.String(required=True)
        author_id = graphene.String(required=True, name="author")

    post = graphene.Field(PostType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **kwargs):
        _post = Post.objects.create(**kwargs)
        return AddPost(post=_post)


class UpdatePost(relay.ClientIDMutation):
    class Input:
        id = graphene.String(required=True)
        title = graphene.String(required=False)
        content = graphene.String(required=False)

    post = graphene.Field(PostType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, pk, title, content):
        try:
            _, pk = from_global_id(pk)
            _post = Post.objects.get(id=pk)
            _post.title = title
            _post.content = content
            _post.updated_at = datetime.utcnow()
            _post.save()
            return UpdatePost(post=_post)
        except Post.DoesNotExist:
            raise http.HTTPStatus.NOT_FOUND


class DeletePost(relay.ClientIDMutation):
    class Input:
        id = graphene.String(required=True)

    success = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, pk):
        try:
            _, pk = from_global_id(pk)
            _post = Post.objects.get(id=pk)
            _post.delete()
            return DeletePost(success=True)
        except Post.DoesNotExist:
            raise http.HTTPStatus.NOT_FOUND


class Mutation(graphene.ObjectType):
    add_post = AddPost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()
