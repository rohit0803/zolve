from django.dispatch import receiver
from django.db import transaction
from django.db.models.signals import post_save

from user.models import WalletUser
from wallet.models import Wallet


@receiver(post_save, sender=WalletUser)
def create_wallet_after_create(sender, instance, created, *args, **kwargs):
    """
    On successful sign up of a new user, we create a wallet for that user.
    """
    if created:
        Wallet.objects.get_or_create(
            user=instance
        )
