from rest_framework import serializers
from reservations.models import Booking
from turf_management.views import Turf
from datetime import datetime

class BookingSerializer(serializers.Serializer):

    id = serializers.CharField(read_only=True)

    name = serializers.CharField()

    phone = serializers.CharField()

    email = serializers.EmailField()

    turf = serializers.CharField()

    match_date = serializers.DateField()

    duration = serializers.IntegerField()

    start_time = serializers.TimeField()

    end_time =serializers.TimeField(read_only=True)

    amount = serializers.IntegerField(read_only=True)


    def create(self,validated_data):

        return Booking.objects.create(**validated_data)

    def update(self, instance, validated_data):

        for attribute,value in validated_data.items():

            setattr(instance,attribute,value)

        return instance

    def validate(self,validated_data):

        duration = validated_data.get("duration")

        if duration not in range(1,5):

            raise serializers.ValidationError("invalid duration time, should be between 1 to 4")

        turf_id = validated_data.get("turf")

        if not Turf.objects.filter(id=turf_id).exists():

            raise serializers.ValidationError("invalid turf it does not exist")

        match_date = validated_data.get("match_date")

        if match_date < datetime.today().date():

            raise serializers.ValidationError("invalid match date")

        return validated_data