from django.urls import path

from wallet import views as wallet_views

urlpatterns = [
    path('users/<int:user_id>/wallet', wallet_views.WalletView.as_view(), name='wallet'),
     path('users/<int:user_id>/wallet/transactions', wallet_views.TransactionsView.as_view(), name='transactions'),
    path('users/<int:user_id>/wallet/debit', wallet_views.Debit.as_view(), name='debit'),
    path('users/<int:user_id>/wallet/credit', wallet_views.Credit.as_view(), name='credit')
]

