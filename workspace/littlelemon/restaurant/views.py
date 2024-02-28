from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    permission_classes = [IsAuthenticated]

class BookingViewSet(ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [IsAuthenticated]