from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .permissions import IsOwnerOrReadOnly
from .serializers import *
from .models import *
# from API.models import User
#from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from ipware import get_client_ip


from rest_framework.pagination import PageNumberPagination


# class CustomPagination(PageNumberPagination):
#     page_size = 20
#     page_size_query_param = 'page_size'
#     max_page_size = 100
#
#
# class MultiModelAPIView(APIView):
#     pagination_class = CustomPagination
#
#     def get(self, request, format=None):
#         model1_data = Player.objects.all()
#         model2_data = Agent.objects.all()
#         model3_data = Club.objects.all()
#         model4_data = Trainer.objects.all()
#
#         serializer1 = PlayerSerializer(model1_data, many=True)
#         serializer2 = AgentSerializer(model2_data, many=True)
#         serializer3 = ClubSerializer(model3_data, many=True)
#         serializer4 = TrainerSerializer(model4_data, many=True)
#         data = {
#             "model1_data": serializer1.data,
#             "model2_data": serializer2.data,
#             "model3_data": serializer3.data,
#             "model4_data": serializer4.data,
#             }
#         paginated_queryset = self.paginate_queryset(data)
#
#         return self.get_paginated_response(paginated_queryset)
class RegisterView(APIView):
    @action(detail=False, methods=['get'], permission_classes=[IsAdminUser], filter_backends=[SearchFilter],
            search_fields=['username'])
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data['role'])
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class AdvancedRegistration_ApiView(viewsets.ModelViewSet):
    lookup_field = 'username'
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, user__username=self.kwargs['username'])
        self.check_object_permissions(self.request, obj)
        return obj

    @action(detail=True, methods=['put'])
    def update_username(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)



class AdvancedRegistration_Player_ApiView(AdvancedRegistration_ApiView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'second_name', 'patronymic','user__username']
    lookup_field = 'username'

    def create(self, request, *args, **kwargs):
        user = request.user
        existing_player = Player.objects.filter(user=user).first()
        if existing_player:
            return Response({'error': 'This user already has a player.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        players = Player.objects.filter(user=user)
        for player in players:
            self.perform_destroy(player)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        username = kwargs.get('username')
        player = get_object_or_404(Player, user__username=username)  # меняем условие поиска на имя пользователя
        # # Получаем IP-адрес пользователя
        # ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        # # Создаем запись о просмотре профиля
        # View.objects.get_or_create(player=player, ip=ip_address)
        serializer = self.get_serializer(player)
        return Response(serializer.data)


class AdvancedRegistration_Agent_ApiView(AdvancedRegistration_ApiView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'second_name', 'patronymic','user__username']
    def create(self, request, *args, **kwargs):
        user = request.user
        existing_agent = Agent.objects.filter(user=user).first()
        if existing_agent:
            return Response({'error': 'This user already has a agent.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        agents = Agent.objects.filter(user=user)
        for agent in agents:
            self.perform_destroy(agent)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        username = kwargs.get('username')
        agent = get_object_or_404(Agent, user__username=username)  # меняем условие поиска на имя пользователя
        # # Получаем IP-адрес пользователя
        # ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        # # Создаем запись о просмотре профиля
        # View.objects.get_or_create(agent=agent, ip=ip_address)
        serializer = self.get_serializer(agent)
        return Response(serializer.data)


class AdvancedRegistration_Trainer_ApiView(AdvancedRegistration_ApiView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'second_name', 'patronymic','user__username']
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    def create(self, request, *args, **kwargs):
        user = request.user
        existing_trainer = Trainer.objects.filter(user=user).first()
        if existing_trainer:
            return Response({'error': 'This user already has a trainer.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        trainers = Trainer.objects.filter(user=user)
        for trainer in trainers:
            self.perform_destroy(trainer)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        username = kwargs.get('username')
        trainer = get_object_or_404(Trainer, user__username=username)  # меняем условие поиска на имя пользователя
        # # Получаем IP-адрес пользователя
        # ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        # # Создаем запись о просмотре профиля
        # View.objects.get_or_create(trainer=trainer, ip=ip_address)
        serializer = self.get_serializer(trainer)
        return Response(serializer.data)


class AdvancedRegistration_Parent_ApiView(AdvancedRegistration_ApiView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'second_name', 'patronymic','user__username']
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    def create(self, request, *args, **kwargs):
        user = request.user
        existing_parent = Parent.objects.filter(user=user).first()
        if existing_parent:
            return Response({'error': 'This user already has a parent.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        parents = Parent.objects.filter(user=user)
        for parent in parents:
            self.perform_destroy(parent)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        username = kwargs.get('username')
        parent = get_object_or_404(Parent, user__username=username)  # меняем условие поиска на имя пользователя
        # # Получаем IP-адрес пользователя
        # ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        # # Создаем запись о просмотре профиля
        # View.objects.get_or_create(parent=parent, ip=ip_address)
        serializer = self.get_serializer(parent)
        return Response(serializer.data)

class AdvancedRegistration_Club_ApiView(AdvancedRegistration_ApiView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    filter_backends = [SearchFilter]
    search_fields = ['national_name', 'eng_name','user__username']
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    def create(self, request, *args, **kwargs):
        user = request.user
        existing_club = Club.objects.filter(user=user).first()
        if existing_club:
            return Response({'error': 'This user already has a club.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        clubs = Club.objects.filter(user=user)
        for club in clubs:
            self.perform_destroy(club)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        username = kwargs.get('username')
        club = get_object_or_404(Club, user__username=username)  # меняем условие поиска на имя пользователя
        # # Получаем IP-адрес пользователя
        # ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        # # Создаем запись о просмотре профиля
        # View.objects.get_or_create(club=club, ip=ip_address)
        serializer = self.get_serializer(club)
        return Response(serializer.data)

class AdvancedRegistration_Scout_ApiView(AdvancedRegistration_ApiView):
    queryset = Scout.objects.all()
    serializer_class = ScoutSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'second_name', 'patronymic','user__username']
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    def create(self, request, *args, **kwargs):
        user = request.user
        existing_scout = Scout.objects.filter(user=user).first()
        if existing_scout:
            return Response({'error': 'This user already has a scout.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        scouts = Scout.objects.filter(user=user)
        for scout in scouts:
            self.perform_destroy(scout)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        username = kwargs.get('username')
        scout = get_object_or_404(Scout, user__username=username)  # меняем условие поиска на имя пользователя
        # # Получаем IP-адрес пользователя
        # ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        # # Создаем запись о просмотре профиля
        # View.objects.get_or_create(scout=scout, ip=ip_address)
        serializer = self.get_serializer(scout)
        return Response(serializer.data)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100
class UserPhotoApiView(viewsets.ModelViewSet):
    serializer_class = UserPhotoSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = UserPhoto.objects.all()
    parser_classes = [MultiPartParser]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        if 'username' in self.kwargs:
            # Если задан username, вернуть фотографии только для этого пользователя
            return UserPhoto.objects.filter(user__username=self.kwargs['username'])
        else:
            # Иначе, вернуть все фотографии
            return UserPhoto.objects.all()

    def list(self, request, *args, **kwargs):
        # Метод list будет обслуживать GET-запросы к коллекции фотографий
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):
        # Get the user object corresponding to the username in the request data
        try:
            user = User.objects.get(username=kwargs['username'])
        except User.DoesNotExist:
            return Response({'error': 'User with username {} not found'.format(request.data['username'])},
                            status=status.HTTP_400_BAD_REQUEST)

        # Create the serializer with the request data and set the user field
        request.data['user'] = user.username
        request.data['role'] = user.role
        serializer = UserPhotoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = user

        # Call serializer.save() to create the UserPhoto object
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        # Get the UserPhoto object associated with the username in the URL
        try:
            user_photo = UserPhoto.objects.get(user=kwargs['username'])
        except UserPhoto.DoesNotExist:
            return Response({'error': 'User photo for user {} not found'.format(kwargs['username'])},
                            status=status.HTTP_404_NOT_FOUND)
        if 'photo' not in request.data:
            serializer = UserPhotoSerializer(user_photo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        request.data['user'] = kwargs['username']
        request.data['role'] = user_photo.user.role
        serializer = UserPhotoSerializer(user_photo, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        # Get the UserPhoto objects associated with the username in the URL
        queryset = UserPhoto.objects.filter(user=kwargs['username'])
        serializer = UserPhotoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        # Get the UserPhoto object associated with the username in the URL
        try:
            user_photo = UserPhoto.objects.get(user=kwargs['username'])
        except UserPhoto.DoesNotExist:
            return Response({'error': 'User photo for user {} not found'.format(kwargs['username'])},
                            status=status.HTTP_404_NOT_FOUND)

        user_photo.delete()
        return Response({'message': 'User photo for user {} has been deleted'.format(kwargs['username'])},
                        status=status.HTTP_204_NO_CONTENT)


class AdvancedRegistration_Video_ApiView(viewsets.ModelViewSet):
    queryset = PlayersVideo.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
        if 'username' in self.kwargs:
            # Если задан username, вернуть видео только для этого пользователя
            return PlayersVideo.objects.filter(user=self.kwargs['username'])
        else:
            # Иначе, вернуть все фотографии
            return PlayersVideo.objects.all()
    def list(self, request, *args, **kwargs):
        # Метод list будет обслуживать GET-запросы к коллекции фотографий
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)



    def create(self, request, *args, **kwargs):
        # Get the user object corresponding to the username in the request data
        try:
            user = User.objects.get(username=kwargs['username'])

        except User.DoesNotExist:
            return Response({'error': 'User with username {} not found'.format(kwargs['username'])},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            player = Player.objects.get(user=user)

        except Player.DoesNotExist:
            return Response({'error': f'Player to username {kwargs["username"]} not found'},
                            status=status.HTTP_400_BAD_REQUEST)


        # Create the serializer with the request data and set the user field
        request.data['user'] = kwargs['username']
        request.data['player'] = player.pk
        request.data['role'] = user.role
        serializer = VideoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = user
        serializer.validated_data['player'] = player

        # Call serializer.save() to create the UserPhoto object
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        # Get the PlayersVideo objects associated with the username in the URL
        queryset = PlayersVideo.objects.filter(user__username=kwargs['username'])
        serializer = VideoSerializer(queryset, many=True)
        if serializer.data == []:
            return Response(
                {'message': 'There are not video for user={}'.format(kwargs['username'])}, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        # Get the PlayersVideo object associated with the username in the URL
        try:
            if 'pk' in self.kwargs:
                user_video = PlayersVideo.objects.get(user__username=kwargs['username'], pk=kwargs['pk'])
                pk = kwargs['pk']
            else:
                user_video = PlayersVideo.objects.filter(user__username=kwargs['username'])
                pk = []
                for video in user_video:
                    pk.append(video.pk)
                    video.delete()

        except PlayersVideo.DoesNotExist:
            return Response({'error': 'Video for user {} not found'.format(kwargs['username'])},
                            status=status.HTTP_404_NOT_FOUND)

        return Response({'message': 'Video (id={}) for user {} has been deleted'.format(pk, kwargs['username'])},
                        status=status.HTTP_204_NO_CONTENT)
