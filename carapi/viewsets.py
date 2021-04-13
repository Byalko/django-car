from rest_framework import viewsets
from .models import Car
from .serializers import CarSerializer
#from rest_framework import filters
#from rest_framework import generics

class CarViewset(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

#class CarViewset(generics.ListAPIView):
#    queryset = Car.objects.all()
#    serializer_class = CarSerializer
#    filter_backends = [filters.SearchFilter]
#    search_fields = ['user_id']