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


class AdvancedRegistration_Trainer_ApiView(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class AdvancedRegistration_Parent_ApiView(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class AdvancedRegistration_Club_ApiView(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class AdvancedRegistration_Scout_ApiView(viewsets.ModelViewSet):
    queryset = Scout.objects.all()
    serializer_class = ScoutSerializer


class AdvancedRegistration_Video_ApiView(viewsets.ModelViewSet):
    queryset = PlayersVideo.objects.all()
    serializer_class = VideoSerializer

