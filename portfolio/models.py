from django.db import models

# Model to represent a cryptocurrency
class Cryptocurrency(models.Model):
    # Name of the cryptocurrency (e.g., 'Bitcoin')
    name = models.CharField(max_length=100)
    
    # Symbol of the cryptocurrency (e.g., 'BTC')
    symbol = models.CharField(max_length=10)
    
    # Current price of the cryptocurrency
    price = models.DecimalField(max_digits=20, decimal_places=10)
    
    # Timestamp of when the record was created
    last_updated = models.DateTimeField(auto_now_add=True)

    # String representation of the model
    def __str__(self):
        return self.name
