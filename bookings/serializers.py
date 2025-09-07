from rest_framework import serializers
from .models import Booking, Payment, Trip

class BookingSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    trip_details = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['booking_reference', 'booking_date', 'user']

        def validate_(self, data):
            trip = data.get('trip')
            seats = data.get('seats', [])

            if not trip:
                raise serializers.ValidationError("Trip is required")
            if not seats:
                raise serializers.ValidationError("At least one seat must be selected")
            
            #Checks if seats are available
            available_seats = trip.available_seats
            for seat in seats:
                if seat not in available_seats:
                    raise serializers.ValidationError(f"seat {seat} is not available")
                return data
            
        def create(self, validated_data):
            #Set current user as the booking user

            validated_data['user'] = self.context['request'].user  

        #calculate total amount 
            trip = validated_data['trip']
            seat_count = len(validated_data['seats'])
            validated_data['total_amount'] = trip.current_price * seat_count

            #create booking
            Booking = super().create(validated_data)

            #update available seats
            trip.available_seats = [seat for seat in trip.available_seats if seat not in validated_data['seats']]
            trip.save()
            return Booking

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Payment
        field = '__all__'
        read_only_fields = ['payment_date']                  
