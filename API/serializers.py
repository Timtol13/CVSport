from rest_framework import serializers
from .models import *
from API.models import User
#from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    # photo = serializers.ImageField(required=False)
    # role = serializers.MultipleChoiceField(max_length=100, required=False)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']  # 'photo']

        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        # user.photo = validated_data.get('photo', '')
        user.role = validated_data.get('role', '')
        user.save()
        return user


class UserPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPhoto
        fields = '__all__'

    def create(self, validated_data):
        photo = UserPhoto.objects.create(
            user=validated_data['user'],
            photo=validated_data['photo']
            # role=validated_data['role'],
        )
        photo.save()
        return photo

    # def update(self, instance, validated_data):
    #     # Валидация и сохранение фото
    #     photo = validated_data.get('photo')
    #     if photo:
    #         instance.photo.delete()  # Удаление предыдущего фото
    #         instance.photo = photo
    #     instance.save()
    #     return instance
    #
    # def destroy(self, instance):
    #     # Удаление фото
    #     instance.photo.delete()
    #     instance.delete()


class PlayerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Player
        fields = '__all__'

    def get_views_count(self, obj):
        return obj.views.count()


class AgentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Agent
        fields = '__all__'


class TrainerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Trainer
        fields = '__all__'


class ParentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Parent
        fields = '__all__'


class ClubSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Club
        fields = '__all__'


class ScoutSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Scout
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PlayersVideo
        fields = '__all__'

    # def create(self, validated_data):
    #     video = PlayersVideo.objects.create(user=validated_data['user'],
    #                                         player=validated_data['player'],
    #                                         video=validated_data['video']
    #                                         # role=validated_data['role'],
    #                                         )
    #     video.save()
    #     return video
    #
    # # def update(self, instance, validated_data):
    # #     # Валидация и сохранение фото
    # #     photo = validated_data.get('photo')
    # #     if photo:
    # #         instance.photo.delete()  # Удаление предыдущего фото
    # #         instance.photo = photo
    # #     instance.save()
    # #     return instance
    # #
    # # def destroy(self, instance):
    # #     # Удаление фото
    # #     instance.photo.delete()
    # #     instance.delete()
    #
    # def get_player(self, obj):
    #     # Получаем данные игрока, связанного с этим видео
    #     player = obj.player
    #     # Сериализуем игрока и возвращаем его данные
    #     return PlayerSerializer(player).data
