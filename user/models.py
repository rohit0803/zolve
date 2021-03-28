from django.db import models


class WalletUser(models.Model):
    """
    Models to store users of Wallet. We have email as unique attribute
    for each user.
    """

    name = models.CharField(
        max_length=100
    )
    email = models.EmailField(
        unique=True
    )
