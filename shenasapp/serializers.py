from rest_framework import serializers
from . import models

from rest_framework.serializers import (
    ModelSerializer,
)

class imageSerializer(ModelSerializer):
    class Meta:
        model = models.MyImage
        fields = [
            'model_pic'
        ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ('name', 'active', 'created')
