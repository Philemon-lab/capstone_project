from django.urls import path
from . import views

urlpatterns = [
    path('agencies/', views.BusAgencyListCreateView.as_view(), name='agency-list'),
    path('agencies/<int:pk>/', views.BusAgencyDetailView.as_view(), name='agency-detail'),
    path('buses/', views.BusListCreateView.as_view(), name='bus-list'),
    path('buses/<int:pk>/', views.BusDetailView.as_view(), name='bus-detail'),
    path('routes/', views.RouteListCreateView.as_view(), name='route-list'),
    path('routes/<int:pk>/', views.RouteDetailView.as_view(), name='route-detail'),
    path('trips/', views.TripListView.as_view(), name='trip-list'),
    path('trips/create/', views.TripCreateView.as_view(), name='trip-create'),
    path('trips/<int:pk>/', views.TripDetailView.as_view(), name='trip-detail'),
]