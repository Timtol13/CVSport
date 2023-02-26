from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .permissions import IsOwnerOrReadOnly
from .serializers import *
from .models import *
# from API.models import User
from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny


# class LoginAPIView(APIView):
#     serializer_class = UserSerializer
#     filter_backends = [SearchFilter]
#     search_fields = ['username']
#     permission_classes = [AllowAny]
#
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

class RegisterView(APIView):
    @action(detail=False, methods=['get'], permission_classes=[IsAdminUser], filter_backends=[SearchFilter],
            search_fields=['username'])
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class AdvancedRegistration_Player_ApiView(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'second_name', 'patronymic', 'position', 'age']
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]


class AdvancedRegistration_Agent_ApiView(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'second_name', 'patronymic']
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]


class AdvancedRegistration_Trainer_ApiView(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'second_name', 'patronymic']
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]


class AdvancedRegistration_Parent_ApiView(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'second_name', 'patronymic']
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]


class AdvancedRegistration_Club_ApiView(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'second_name', 'patronymic']
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]


class AdvancedRegistration_Scout_ApiView(viewsets.ModelViewSet):
    queryset = Scout.objects.all()
    serializer_class = ScoutSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'second_name', 'patronymic']
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]


class AdvancedRegistration_Photo_ApiView(viewsets.ModelViewSet):
    queryset = UserPhoto.objects.all()
    serializer_class = UserPhotoSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Get the user object corresponding to the username in the request data

        try:
            user = User.objects.get(username=request.data['user'])

            print(user)
        except User.DoesNotExist:
            return Response({'error': 'User with username {} not found'.format(request.data['username'])},
                            status=status.HTTP_400_BAD_REQUEST)

        # Create the serializer with the request data and set the user field
        id = user.pk
        print(request.data)
        request.data['user']=id
        print(request.data)
        serializer = UserPhotoSerializer(data=request.data)
        serializer.is_valid()

        # Call serializer.save() to create the UserPhoto object

        serializer.save()
        print(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def update(self, request, *args, **kwargs):
        print(request.user)
        print(self.request)
        instance = self.get_object()  #
        print(instance)
        serializer = self.get_serializer(instance, data=request.data, partial=False)  #
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)  #
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdvancedRegistration_Video_ApiView(viewsets.ModelViewSet):
    queryset = PlayersVideo.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]
