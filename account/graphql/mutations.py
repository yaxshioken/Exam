import graphene
import graphql_jwt
from graphql import GraphQLError
from rest_framework.generics import get_object_or_404

from account.graphql.mutates import create_user_mutate, create_login_mutate
from account.graphql.types import UserType
from account.models import User


# class LoginMutation(graphene.Mutation):
#     class Arguments:
#         username = graphene.String(required=True)
#         password = graphene.String(required=True)
#         user = graphene.Field(lambda: UserType)
#         @classmethod
#         def mutate(cls, root, info, username, password):
#             user=get_object_or_404(User, username=username)
#             if not user.check_password(password):
#                 raise GraphQLError("Password incorrect")
#             else:
#                 return LoginMutation(user)


class RegisterUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()
        password2 = graphene.String()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = create_user_mutate(**kwargs)
        return RegisterUser(user=user)


class Mutation(graphene.ObjectType):
    register_user = RegisterUser.Field()
    # login = LoginMutation.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
