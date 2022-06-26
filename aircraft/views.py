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

        q = Aircraft.objects.all()
        tags = None
        if self.request.query_params.get('tag'):
            tags = self.request.query_params.get('tag').split(',')
        
        ql = []
        if tags:
            for t in tags:
                ql.append(q.filter(tags__contains=t))
            qo = ql[0]
            for qs in ql[1:]:
                qo = qo | qs
            return qo
        return q
    renderer_classes = [JSONRenderer]
    serializer_class = AircraftSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields= ['model', 'atct_weight_class']
