from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from auth_util.token import decode_token


class CustomAuth(ModelBackend):

    def authenticate(self, request, username=None, password=None):
        token = request.GET.get('token')
        if token is None:
            return None
        decoded = decode_token(token)
        username = decoded['sub']

        try:
            user = User.objects.get(username=username)
            if not user.is_staff or not user.is_superuser or not user.is_active:
                return None
        except User.DoesNotExist:
            user = User(username=username)
            user.is_staff = True
            user.is_superuser = True
            user.save()
        return user



    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

