from django.shortcuts import render
from rest_framework import viewsets
from . import models
from shenasapp import serializers
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, )
from rest_framework.permissions import IsAuthenticated
from .models import userProfile
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import userProfileSerializer


class UserProfileListCreateView(ListCreateAPIView):
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class userProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


class personalImageView(viewsets.ModelViewSet):
    serializer_class = serializers.prsonalImageSerializer
    queryset = models.PersonallyImage.objects.all()


class nationalCardImageView(viewsets.ModelViewSet):
    serializer_class = serializers.nationalCarImageSerializer
    queryset = models.NationalCardImage.objects.all()


class shenasnameImageView(viewsets.ModelViewSet):
    serializer_class = serializers.shenasnameCardImageSrializer
    queryset = models.ShenasnameImage.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    # this fetches all the rows of data in the Fish table
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
