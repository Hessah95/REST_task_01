from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .serializers import FlightSerializers, BookingSerializers
from django.utils import timezone


class Flights (ListAPIView) :
    queryset = Flight.objects.all()
    serializer_class = FlightSerializers


class Bookings (ListAPIView) :
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers