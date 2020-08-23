from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, EmotionSerializer, EmotionPairSerializer

from .models import Emotion, EmotionPair

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class EmotionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows emotions to be viewed or edited.
    """
    queryset = Emotion.objects.all().order_by('name')
    serializer_class = EmotionSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmotionPairViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows emotion pairs to be viewed or edited.
    """
    queryset = EmotionPair.objects.all().order_by('name')
    serializer_class = EmotionPairSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
