from rest_framework import serializers
from . import models

from rest_framework.serializers import (
    ModelSerializer,
)


class userProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.userProfile
        fields = '__all__'


class imageSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=models.User.objects.all(), source='User.id')

    class Meta:
        model = models.PersonallyImage
        fields = ("model_pic")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ['name', "lastName", "nationalCode", "shenasnameCode", 'created']

    def get_tracks(self, user):
        qs = user.personallyimage_set.all()[-1:]
        return imageSerializer(qs, many=True, read_only=True).data
