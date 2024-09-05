from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cryptocurrency
from .serializers import CryptocurrencySerializer
from rest_framework.permissions import IsAuthenticated


class FetchCryptoData(APIView):  # View to fetch and store cryptocurrency data from an external API
    
    permission_classes = [IsAuthenticated]  # Require authentication to access this view

    def get(self, request):
        
        api_url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false'   # URL of the external API providing cryptocurrency data
        response = requests.get(api_url)  # Send a GET request to the external API

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Iterate through the fetched data and update or create cryptocurrency records
            for item in data:
                Cryptocurrency.objects.update_or_create(
                    symbol=item['symbol'],
                    defaults={
                        'name': item['name'],
                        'price': item['current_price'],
                    }
                )
            # Return a success message
            return Response({"message": "Data fetched and stored successfully!"}, status=status.HTTP_200_OK)
        else:
            # Return an error message if the request failed
            return Response({"error": "Failed to fetch data"}, status=status.HTTP_400_BAD_REQUEST)

# View to list all stored cryptocurrencies
class CryptoListView(APIView):
    # Require authentication to access this view
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Retrieve all cryptocurrency records from the database
        cryptocurrencies = Cryptocurrency.objects.all()
        # Serialize the retrieved data
        serializer = CryptocurrencySerializer(cryptocurrencies, many=True)
        # Return the serialized data
        return Response(serializer.data)
