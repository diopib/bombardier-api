# from django.conf.urls import include
from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views as core_views

router = routers.SimpleRouter()
public_router = routers.SimpleRouter()

router.register(r'aircraft', core_views.AircraftViewset, basename="aircraft")

urlpatterns = [
    path(r'', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
