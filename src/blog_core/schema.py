import graphene

from blog_site.queries.post import Query as PostQuery
from blog_site.queries.author import Query as AuthorQuery

from blog_site.mutations.author import Mutation as AuthorMutation
from blog_site.mutations.post import Mutation as PostMutation


class Query(PostQuery, AuthorQuery, graphene.ObjectType):
    pass


class Mutation(AuthorMutation, PostMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
