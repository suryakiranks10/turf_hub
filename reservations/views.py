from django.shortcuts import render
from reservations.models import Booking
# Create your views here.
from rest_framework.views import APIView
from reservations.serializers import BookingSerializer
from rest_framework.response import Response
from datetime import datetime,timedelta,time
from turf_management.models import Turf
from rest_framework import authentication,permissions

class BookingCreateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]


    def post(self,request):

        form_data = request.data

        serializer_instance = BookingSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            start_time = cleaned_data.get("start_time")

            duration = cleaned_data.get("duration")

            match_date = cleaned_data.get("match_date")

            end_date_time = datetime.combine(match_date,start_time)+timedelta(hours=duration)

#to take time only from end date time we only need ending time
            end_time = end_date_time.time()

#took the turf id from data we send
            turf_id = cleaned_data.get("turf")

#took the turf from turf id sended
            turf_object = Turf.objects.get(id=turf_id)

#change time which was int into time so it can compare 
            if start_time > time(18,0):

                amount = turf_object.night_price*duration

            else:
                
                amount = turf_object.day_price*duration

            booking_objects = Booking.objects.filter(
                turf = cleaned_data.get("turf"),
                match_date = cleaned_data.get("match_date"),
                start_time__lt = end_time,    #left side is current right side is new end time and start time
                end_time__gt = start_time    

            )

            if booking_objects.exists():

                return Response({"message":"slot is not available"})
            

# need to add end_time and amount because they were read only so need to add extra
            serializer_instance.save(end_time=end_time,amount=amount)

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)


class BookingSummaryView(APIView):

    def post(self,request):

        form_data = request.data

        turf = form_data.get("turf")

        match_date = datetime.strptime(form_data.get("match_date"),"%Y-%m-%d")

        bookings = Booking.objects.filter(turf=turf,match_date=match_date)

        serializer_instance = BookingSerializer(bookings,many=True)

        return Response(serializer_instance)


class BookingRetrieveUpdateDeleteView(APIView):


    def get(self,request,pk=None):

        qs=Booking.objects.get(id=pk)

        serializer_instance = BookingSerializer(qs)

        return Response(serializer_instance.data)


    def put(self,request,pk=None):

        turf_object = Booking.objects.get(id=pk)

        form_data = request.data

        serializer_instance = BookingSerializer(data=form_data,instance=turf_object)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            start_time = cleaned_data.get("start_time")

            match_date = cleaned_data.get("match_date")

            duration = cleaned_data.get("duration")

            end_date_time =datetime.combine(start_time,match_date)+timedelta(hours=duration)

            end_time = end_date_time.time() 

            serializer_instance.save(end_time=end_time)

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors) 


    def delete(self,request,pk=None):

        Booking.objects.filter(id=pk).delete()

        return Response({"message deleted"})
    
        