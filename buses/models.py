from django.db import models
from django.conf import settings

class BusAgency(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    address = models.TextField()
    logo = models.ImageField(upload_to='agency_logos/', null=True, blank=True)
    rating = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='agencies')
    def __str__(self):
        return self.name
    
class Bus(models.Model):
    Bus_TYPES = (
        ('standart', 'standard'),
        ('luxury', 'vip')
        ('sleeper', 'sleeper')
    )
    agency = models.ForeignKey(BusAgency, on_delete=models.CASCADE, related_name='buses')
    bus_number = models.CharField(max_length=20)
    bus_type = models.CharField(max_length=20)
    total_seats = models.PositiveIntegerField()
    amenities = models.JSONField(default=list)

    def __str__(self):
        return f"{self.bus_number} ({self.agency.name})"
