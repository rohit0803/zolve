from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.exceptions import ParseError,NotFound
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

from wallet import (
    models as wallet_models,
    serializers as wallet_serializer,
    exceptions as wallet_exceptions
)


class WalletView(RetrieveAPIView):
    """
    API for deatils of wallet.
    """
    queryset = wallet_models.Wallet.objects.all()
    serializer_class = wallet_serializer.WalletSerializer

    lookup_field  = 'user_id'


class Debit(APIView):
    """
    API for debit of money from wallet.
    """
    def post(self, request, *args, **kwargs):
        data = request.data
        amount = data.get('amount')
        if not amount or not (isinstance(amount, int) or isinstance(amount, float)):
            raise ParseError()

        wallet = wallet_models.Wallet.objects.filter(
            user_id=kwargs.get('user_id')
        ).first()

        if not wallet:
            raise NotFound()

        try:
            wallet = wallet.debit(amount)
        except wallet_exceptions.TransactionFailed:
            raise ParseError("Cannot perform transaction.")

        serializer = wallet_serializer.WalletSerializer(instance=wallet)
        if not serializer.is_valid:
            raise ParseError()
        return Response(serializer.data)


class Credit(APIView):
    """
    API for credit of money to wallet.
    """
    def post(self, request, *args, **kwargs):
        data = request.data
        amount = data.get('amount')
        if not amount or not (isinstance(amount, int) or isinstance(amount, float)):
            raise ParseError()

        wallet = wallet_models.Wallet.objects.filter(
            user_id=kwargs.get('user_id')
        ).first()

        if not wallet:
            raise NotFound()

        try:
            wallet = wallet.credit(amount)
        except wallet_exceptions.TransactionFailed:
            raise ParseError("Cannot perform transaction.")

        serializer = wallet_serializer.WalletSerializer(instance=wallet)
        if not serializer.is_valid:
            raise ParseError()
        return Response(serializer.data)


class TransactionsView(ListAPIView):
    """
    API for list of transactions from wallet.
    """
    queryset = wallet_models.Transactions.objects.all()
    serializer_class = wallet_serializer.TransactionsSerializer
    pagination_serializer_class = LimitOffsetPagination

    def filter_queryset(self, queryset):

        user_id = self.kwargs.get('user_id')
        if not user_id:
            raise NotFound()

        queryset =queryset.filter(user_id=user_id)

        return queryset
