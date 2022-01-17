from rest_framework import serializers
from .models import Coffee

class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "maker", "description", "created_at")
        model = Coffee