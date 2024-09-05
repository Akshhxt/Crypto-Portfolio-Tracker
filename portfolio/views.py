from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import requests

from .models import Cryptocurrency
from .serializers import CryptocurrencySerializer

# Home view for the root URL
def home(request):
    return HttpResponse("<h1>Welcome to the Crypto Portfolio Tracker</h1><p>Use the API endpoints to interact with the application.</p>")

# View to fetch cryptocurrency data from a third-party API
class FetchCryptoData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # URL for fetching data from a third-party cryptocurrency API
        api_url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false'
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            for item in data:
                Cryptocurrency.objects.update_or_create(
                    symbol=item['symbol'],
                    defaults={
                        'name': item['name'],
                        'price': item['current_price'],
                    }
                )
            return Response({"message": "Data fetched and stored successfully!"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Failed to fetch data"}, status=status.HTTP_400_BAD_REQUEST)

# View to display the list of cryptocurrencies stored in the database
class CryptoListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cryptocurrencies = Cryptocurrency.objects.all()
        serializer = CryptocurrencySerializer(cryptocurrencies, many=True)
        return Response(serializer.data)
