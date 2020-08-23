from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Emotion, EmotionPair

class EmotionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Emotion
        fields = ['name', 'family', 'description']

class EmotionPairSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmotionPair
        fields = ['name', 'left', 'right']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
