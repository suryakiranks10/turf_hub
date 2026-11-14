from django.shortcuts import render

# Create your views here. 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from turf_management.models import Turf
from turf_management.serializers import TurfSerializer

class TurfListCreateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def get(self,request):

        qs=Turf.objects.all()

        serializer_instance=TurfSerializer(qs,many=True)

        return Response(serializer_instance.data)

    def post(self,request):

        form_data=request.data

        serializer_instance=TurfSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(serializer_instance.data)
        
        else:

            return Response(serializer_instance.errors)   


class TurfRetriveUpdateDeleteView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAdminUser]
    

    def get(self,request,pk=None):

        qs=Turf.objects.get(id=pk)

        serializer_instance=TurfSerializer(qs)

        return Response(serializer_instance.data)

    def put(self,request,pk=None):

        turf_object=Turf.objects.get(id=pk)

        form_data=request.data

        serializer_instance=TurfSerializer(data=form_data,instance=turf_object)

        if serializer_instance.is_valid():

            serializer_instance.save()   #update will work because instance is given

            return Response(serializer_instance.data)
        
        else:

            return Response(serializer_instance.errors)
        

    def delete(self,request,pk=None):

        Turf.objects.get(id=pk).delete()

        return Response({"message":"deleted"}) 