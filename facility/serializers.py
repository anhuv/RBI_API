from rest_framework import serializers

from facility.models import Facility


class FacilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Facility
        fields = ('facilityid', 'siteid', 'facilityname', 'managementfactor', 'managementfactor', 'create', 'time') 
        
