from rest_framework.generics import get_object_or_404

from account.models import User


def create_user_mutate(username, password, password2, email):
    if password != password2:
        raise Exception("passwords must be match")
    if User.objects.filter(username=username).exists():
        raise Exception(f"{username} username already registered")
    user = User.objects.create_user(username=username, email=email)
    user.set_password(password)
    user.save()
    return user
def create_login_mutate(username, password):
    user=get_object_or_404(User, username=username)
    if user.check_password(password):
        return user
    else:
        raise Exception("password must be match")