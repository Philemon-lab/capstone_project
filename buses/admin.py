from django.contrib import admin
from .models import BusAgency, Bus, Trip, Trip, Route

admin.site.register(BusAgency)
admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(Trip)

