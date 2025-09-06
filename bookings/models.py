from django.db import models
from django.conf import settings
from buses.models import Trip
import random
import string

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookingd')
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='bookings')
    booking_reference = models.CharField(max_length=100, unique=True)
    seats =models.JSONField(default=list)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=(
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
        ('completed', 'Completed'),
    ), default='confirmed')
    cancelation_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.booking_reference:
            self.booking_reference = self.generate_booking_reference()
        super().save(*args, **kwargs)

    def generate_booking_reference(self):
        while True:
            ref = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            if not Booking.objects.filter(booking_reference=ref).exists():
                return ref
            
    def __str__(self):
        return f"Booking {self.booking_reference} by {self.user.username}"
    
class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='payment')
    Payment_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    status = models.CharField(max_length=20, choices=(
        ('pending','Pendig'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ), default='pending')
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.booking.booking_reference}"
