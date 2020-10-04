from rest_framework import serializers
from . import models

from rest_framework.serializers import (
    ModelSerializer,
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ('name', "lastName", "nationalCode", "shenasnameCode", 'created',"accepted")
    #
    # def get_tracks(self, user):
    #     qs = user.personallyimage_set.all()[-1:]
    #     return prsonalImageSerializer(qs, many=True, read_only=True).data


class userProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.userProfile
        fields = '__all__'


class prsonalImageSerializer(serializers.ModelSerializer):
    user = userProfileSerializer

    class Meta:
        model = models.PersonallyImage
        fields = ("model_pic", "user",)


class nationalCarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NationalCardImage
        fields = ("model_pic", "user")


class shenasnameCardImageSrializer(serializers.ModelSerializer):
    class Meta:
        model = models.ShenasnameImage
        fields = ("model_pic", "user")
