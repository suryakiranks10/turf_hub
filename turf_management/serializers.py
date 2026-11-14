from rest_framework import serializers
from turf_management.models import Turf

class TurfSerializer(serializers.Serializer):

    id = serializers.CharField(read_only=True)

    name = serializers.CharField()

    location = serializers.CharField()

    address = serializers.CharField()

    description = serializers.CharField()

    opening_time = serializers.TimeField()

    closing_time = serializers.TimeField()

    day_price = serializers.DecimalField(max_digits=10,decimal_places=2)

    night_price = serializers.DecimalField(max_digits=10,decimal_places=2)

    facilities = serializers.CharField()


    def create(self, validated_data):
        return Turf.objects.create(**validated_data)

#here we take instance as the turf which needs to be updated by this way create and update are different update will have instance and create doesnt
    def update(self, instance, validated_data):

#items used to get key and value of dict as it is dict method
        for attribute,value in validated_data.items():   

#              whichever id   its key   which value to update
            setattr(instance,attribute,value)

            return instance