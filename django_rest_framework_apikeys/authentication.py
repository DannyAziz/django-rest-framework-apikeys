from django.contrib.auth.models import User
from rest_framework import authentication, exceptions


class APIKeyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        api_key = request.META.get("HTTP_X_API_KEY", None)

        if not api_key:
            return None

        try:
            user = User.objects.get(apikey__key=api_key)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such User')

        return (user, None)


    def authenticate_header(self, request):
        return "API_KEY"