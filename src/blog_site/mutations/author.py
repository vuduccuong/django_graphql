import http

import graphene
from graphene import relay
from graphql_relay import from_global_id

from blog_site.models import Author
from blog_site.types import AuthorType


class AddAuthor(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        bio_data = graphene.String()

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **kwargs):
        _author = Author.objects.create(**kwargs)
        return AddAuthor(author=_author)


class UpdateAuthor(relay.ClientIDMutation):
    class Input:
        id = graphene.String(required=True)
        name = graphene.String(required=True)
        bio_data = graphene.String(required=True)

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **kwargs):
        pk = kwargs.get("id")
        name = kwargs.get("name")
        bio_data = kwargs.get("bio_data")

        try:
            _, pk = from_global_id(pk)
            _author = Author.objects.get(id=pk)
            _author.name = name
            _author.bio_data = bio_data
            _author.save()

            return UpdateAuthor(author=_author)
        except Author.DoesNotExist:
            raise http.HTTPStatus.NOT_FOUND


class DeleteAuthor(relay.ClientIDMutation):
    class Input:
        id = graphene.String(required=True)

    success = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, pk):
        try:
            _, pk = from_global_id(pk)
            _author = Author.objects.get(id=pk)
            _author.delete()
            return DeleteAuthor(success=True)
        except Author.DoesNotExist:
            raise http.HTTPStatus.NOT_FOUND


class Mutation(graphene.ObjectType):
    add_author = AddAuthor.Field()
    update_author = UpdateAuthor.Field()
    delete_author = DeleteAuthor.Field()
