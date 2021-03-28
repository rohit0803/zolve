from django.db import models
from django.conf import settings

from user.models import WalletUser
from wallet import constants
from wallet.exceptions import TransactionFailed


class Wallet(models.Model):
    """
    Model to maintain balance.
    """
    user = models.OneToOneField(
        WalletUser,
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )

    def __str__(self):
        return self.user_id

    def debit(self, amount):
        """
        Method for debit of money from wallet.
        """
        rows_updated = Wallet.objects.filter(
            id=self.id,
            balance__gte=(
                constants.MINIMUM_BALANCE + amount
            )
        ).update(
            balance=models.F('balance') - amount
        )

        if not rows_updated:
            raise TransactionFailed()

        self.refresh_from_db()
        self.add_transaction('debit', amount)
        return self

    def credit(self, amount):
        """
        Method for credit of money to wallet.
        """
        Wallet.objects.filter(
            id=self.id
        ).update(
            balance=models.F('balance') + amount
        )

        self.refresh_from_db()
        self.add_transaction('credit', amount)
        return self

    def add_transaction(self, type, amount):
        type_map = {
            "credit": "amout_credited",
            "debit": "amout_debited"
        }

        key =type_map.get(type, '')

        if not key:
            return

        transaction = Transactions.objects.create(
            user=self.user,
            balance=self.balance
        )

        setattr(
            transaction,
            key,
            amount
        )

        transaction.save()


class Transactions(models.Model):

    user = models.ForeignKey(
        WalletUser,
        on_delete=models.CASCADE
    )
    transaction_date = models.DateTimeField(
        auto_now_add=True
    )
    amout_debited = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    amout_credited = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
