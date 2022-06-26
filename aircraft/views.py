from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from aircraft.models import Aircraft
from aircraft.serializers import AircraftSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.renderers import JSONRenderer

# Create your views here.

class AircraftViewset(viewsets.ModelViewSet):
    """A viewset for Listing Aircraft"""

    def get_queryset(self):
        tag = self.request.query_params.get('tag')
        if tag:
            return Aircraft.objects.filter(tags__contains=tag)
        else:
            return Aircraft.objects.all()
    renderer_classes = [JSONRenderer]
    serializer_class = AircraftSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields= ['model', 'atct_weight_class']
