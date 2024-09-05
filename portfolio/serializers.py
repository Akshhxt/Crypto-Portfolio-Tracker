from rest_framework import serializers
from .models import Cryptocurrency

# Serializer for the Cryptocurrency model
class CryptocurrencySerializer(serializers.ModelSerializer):
    class Meta:
        # Specify the model to be serialized
        model = Cryptocurrency
        # Include all fields from the Cryptocurrency model
        fields = '__all__'