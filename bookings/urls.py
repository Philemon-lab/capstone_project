from django.urls import path
from . import views

urlpatterns = [
    path('bookings/', views.BookingListCreateView.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', views.BookingDetailView.as_view(), name='booking-detail'),
    path('bookings/<int:booking_id>/payment/', views.create_payment, name='create-payment'),
]