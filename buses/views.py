from rest_framework import generics, permissions
from .models import BusAgency, Bus, Route, Trip
from .serializers import BusAgencySerializer, BusSerializer, RouteSerializer, TripSerializer

class IsAgencyStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['agency_staff', 'admin']

class BusAgencyListCreateView(generics.ListCreateAPIView):
    queryset = BusAgency.objects.all()
    serializer_class = BusAgencySerializer
    permission_classes = [permissions.IsAuthenticated, IsAgencyStaff]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BusAgencyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BusAgency.objects.all()
    serializer_class = BusAgencySerializer
    permission_classes = [permissions.IsAuthenticated, IsAgencyStaff]

class BusListCreateView(generics.ListCreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    permission_classes = [permissions.IsAuthenticated, IsAgencyStaff]

class BusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    permission_classes = [permissions.IsAuthenticated, IsAgencyStaff]

class RouteListCreateView(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticated, IsAgencyStaff]

class RouteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticated, IsAgencyStaff]

class TripListView(generics.ListAPIView):
    queryset = Trip.objects.filter(status='scheduled')
    serializer_class = TripSerializer
    permission_classes = [permissions.AllowAny]

class TripCreateView(generics.CreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated, IsAgencyStaff]

class TripDetailView(generics.RetrieveAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [permissions.AllowAny]