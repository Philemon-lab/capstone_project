from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Booking, Payment
from .serializers import BookingSerializer, PaymentSerializer

class BookingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Users can only see their own bookings
        return Booking.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer_class = BookingSerializer
        permission_class = [permissions.IsAuthenticated]

        def get_queryset(self):
            return Booking.objects.filter(user=self.request.user)
        
@api_view(['POST'])
def create_payment(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id, user=request.user)
    except Booking.DoesNotExist:
        return Response(
            {"erro": "Booking not found"}, status=status.HTTP_404_NOT_FOUND
        )
#Simulate a successful payment
    payment_data = {
        'booking': booking.id,
        'payment_method': request.data.get('payment_method', 'card'),
        'amount':
        booking.total_amount,
        'status' : 'completed',
        'transaction_id': f"simulated_{booking.booking_reference}"
    }

    serializer = PaymentSerializer(data=payment_data)
    if serializer.is_valid():
        payment = serializer.save()
        return Response(PaymentSerializer(payment).data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
