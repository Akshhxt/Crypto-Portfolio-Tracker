from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import requests

from .models import Cryptocurrency
from .serializers import CryptocurrencySerializer

# View to render the home page
def home(request):
    return render(request, 'portfolio/home.html')


# View to fetch cryptocurrency data from a third-party API and store it in the database
class FetchCryptoData(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

    def get(self, request):
        # URL for fetching data from a third-party cryptocurrency API (CoinGecko)
        api_url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false'
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            for item in data:
                # Save or update data in the database
                Cryptocurrency.objects.update_or_create(
                    symbol=item['symbol'],
                    defaults={
                        'name': item['name'],
                        'price': item['current_price'],
                        'change': item.get('price_change_percentage_24h', 0),
                        'volume': item.get('total_volume', 0),
                        'market_cap': item.get('market_cap', 0),
                        'icon_url': item.get('image', ''),
                    }
                )
            return Response({"message": "Data fetched and stored successfully!"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Failed to fetch data from the API"}, status=status.HTTP_400_BAD_REQUEST)


# View to expose a REST API endpoint that lists all stored cryptocurrencies
class CryptoListView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

    def get(self, request):
        # Retrieve all cryptocurrencies from the database
        cryptocurrencies = Cryptocurrency.objects.all()
        serializer = CryptocurrencySerializer(cryptocurrencies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
