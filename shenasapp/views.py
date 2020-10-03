from django.shortcuts import render
from rest_framework import viewsets
from . import models
from shenasapp import serializers


class ImageCreateAPIView(viewsets.ModelViewSet):
    serializer_class = serializers.imageSerializer
    queryset = models.MyImage.objects.all()


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    # this fetches all the rows of data in the Fish table
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
