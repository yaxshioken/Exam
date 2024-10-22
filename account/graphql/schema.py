import graphene

from account.graphql.mutations import Mutation
from account.graphql.query import Query

schema = graphene.Schema(query=Query, mutation=Mutation)

__all__ =("schema",)