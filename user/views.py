from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, ParseError

from user import (
    models as user_models,
    serializers as user_serializer
)


class SignUp(CreateAPIView):
    """
    API for signup of new user.
    """

    queryset = user_models.WalletUser.objects.all()
    serializer_class = user_serializer.UserSerializer


class SignIn(APIView):
    """
    API for signin of user.
    """

    def post(self, request, *args, **kwargs):

        data = request.data
        email = data.get('email', '')
        if not email:
            raise AuthenticationFailed()

        user = user_models.WalletUser.objects.filter(
            email=email
        ).first()
        if not user:
            raise AuthenticationFailed()

        serializer = user_serializer.UserSerializer(instance=user)

        if not serializer.is_valid:
            raise ParseError()

        return Response(serializer.data)
