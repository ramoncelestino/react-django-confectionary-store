from django.db.models import fields
from .models import Customer, Order, City, Neighborhood
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name']

class NeighborhoodSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    class Meta:
        model = Neighborhood
        fields = ['name', 'city']

class CustomerSerializer(serializers.ModelSerializer):
    neighborhood = NeighborhoodSerializer()
    class Meta:
        model = Customer
        fields = '__all__'