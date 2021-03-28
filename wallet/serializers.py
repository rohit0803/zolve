from rest_framework import serializers

from wallet import (
    models as wallet_models
)
from user.serializers import UserSerializer


class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = wallet_models.Wallet
        fields = [
            "balance",
            "created"
        ]


class TransactionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = wallet_models.Transactions
        fields = [
            "transaction_date",
            "amout_debited",
            "amout_credited",
            "balance"
        ]