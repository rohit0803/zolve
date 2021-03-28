from rest_framework import serializers

from user import models as user_models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_models.WalletUser
        fields = [
            "id",
            "name",
            "email"
        ]
