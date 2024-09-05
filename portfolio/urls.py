from django.urls import path
from .views import home, FetchCryptoData, CryptoListView

urlpatterns = [
    path('', home, name='home'),
    # URL pattern for fetching and storing cryptocurrency data
    path('api/fetch/', FetchCryptoData.as_view(), name='fetch_crypto_data'),

    # URL pattern for listing all stored cryptocurrencies
    path('api/cryptocurrencies/', CryptoListView.as_view(), name='crypto_list'),
]
