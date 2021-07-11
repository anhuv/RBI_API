from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import permissions

from django.shortcuts import redirect, render

from facility.models import Facility
from facility.serializers import FacilitySerializer

# Create your views here.
def home_view(request):
    return render(request, 'home.html') 

class ListCreateFacilityView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    model = Facility
    serializer_class = FacilitySerializer

    def get_queryset(self):
        return Facility.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = FacilitySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Car successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Car unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteFacilityView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    model = Facility
    serializer_class = FacilitySerializer

    def put(self, request, *args, **kwargs):
        car = get_object_or_404(Facility, id=kwargs.get('pk'))
        serializer = FacilitySerializer(car, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Car successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Car unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        car = get_object_or_404(Facility, id=kwargs.get('pk'))
        car.delete()

        return JsonResponse({
            'message': 'Delete Car successful!'
        }, status=status.HTTP_200_OK) 