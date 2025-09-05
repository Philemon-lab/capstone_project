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
        ('standard', 'Standard'),
        ('luxury', 'Luxury'),
        ('sleeper', 'Sleeper'),
    )
    agency = models.ForeignKey(BusAgency, on_delete=models.CASCADE, related_name='buses')
    bus_number = models.CharField(max_length=20)
    bus_type = models.CharField(max_length=20)
    total_seats = models.PositiveIntegerField()
    amenities = models.JSONField(default=list)

    def __str__(self):
        return f"{self.bus_number} ({self.agency.name})"

class Route(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    distance = models.DurationField(help_text="Estimated traval time")
    intermediate_stops = models.JSONField(default=list)

    def __str__(self):
        return f"{self.origin} to {self.destination}"
    

class Trip(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='trips')
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='trips')
    departure_time = models.DateTimeField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seates = models.JSONField(default=list)
    status = models.CharField(max_length=20,choices=(
        ('scheduled', 'Scheduled'),
        ('boarding', 'Boarding'),
        ('departed', 'Departed'),
        ('arrived', 'Arrived'),
        ('canceled', 'Canceled')
    ), default='scheduled'
    )

    def __str__(self):
        return f"{self.bus.bus_number} - {self.route} -{self.departure_time}"