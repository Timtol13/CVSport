from rest_framework import viewsets
from .serializers import *
from .models import *
from django.contrib.auth.models import User


class RegistrationAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AdvancedRegistration_Player_ApiView(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class AdvancedRegistration_Agent_ApiView(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class AdvancedRegistration_Video_ApiView(viewsets.ModelViewSet):
    queryset = PlayersVideo.objects.all()
    serializer_class = VideoSerializer

