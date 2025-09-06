from rest_framework import serializers
from .models import BusAgency, Bus, Route, Trip

class BusAgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusAgency
        fields = '__all__'
        read_only_fields = ['owner', 'rating']

class BusSerializer(serializers.ModelSerializer):
    agency_name = serializers.CharField(source='agency.name', read_only=True)

    class Meta:
        model = Bus
        field = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    bus_datails = BusSerializer(source='bus', read_only=True)
    route_details = RouteSerializer(source='route', read_only=True)
    available_seats_count = serializers.SerializerMethodField()

    class Meta:
        model = Trip
        fields = '__all__'

    def get_available_seats_count(self, obj):
        return len(obj.available_seates)