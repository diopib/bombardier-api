from rest_framework import serializers
import aircraft.models as am

class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = am.Aircraft
        fields = '__all__'
