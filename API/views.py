from rest_framework import viewsets
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter

class RegistrationAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    search_fields = ['username']

class AdvancedRegistration_Player_ApiView(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'second_name', 'patronymic']

class AdvancedRegistration_Agent_ApiView(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'second_name', 'patronymic']


class AdvancedRegistration_Trainer_ApiView(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'second_name', 'patronymic']


class AdvancedRegistration_Parent_ApiView(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'second_name', 'patronymic']


class AdvancedRegistration_Club_ApiView(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'second_name', 'patronymic']


class AdvancedRegistration_Scout_ApiView(viewsets.ModelViewSet):
    queryset = Scout.objects.all()
    serializer_class = ScoutSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'second_name', 'patronymic']


class AdvancedRegistration_Video_ApiView(viewsets.ModelViewSet):
    queryset = PlayersVideo.objects.all()
    serializer_class = VideoSerializer

