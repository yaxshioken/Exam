import graphene

from account.graphql.types import UserType




class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    user = graphene.Field(UserType)

