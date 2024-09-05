from django.urls import path
from .views import FetchCryptoData, CryptoListView

urlpatterns = [
    # URL pattern for fetching and storing cryptocurrency data
    path('fetch/', FetchCryptoData.as_view(), name='fetch_crypto_data'),

    # URL pattern for listing all stored cryptocurrencies
    path('cryptocurrencies/', CryptoListView.as_view(), name='crypto_list'),
]
