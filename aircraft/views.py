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
        tags = self.request.query_params.get('tag').split(',')
        print(tags)
        q = Aircraft.objects.all()
        ql = []
        if tags:
            for t in tags:
                ql.append(q.filter(tags__contains=t))

        return q.union(*ql)
    renderer_classes = [JSONRenderer]
    serializer_class = AircraftSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields= ['model', 'atct_weight_class']
