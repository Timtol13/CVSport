from rest_framework import serializers
from .models import *
# from API.models import UserData
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    # photo = serializers.ImageField(required=False)
    # role = serializers.MultipleChoiceField(max_length=100, required=False)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', ]  # 'photo' #, 'role']

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
            photo=validated_data['photo'],
            #role=validated_data['role'],
        )
        photo.save()
        return photo

    def update(self, instance, validated_data):
        # Валидация и сохранение фото
        photo = validated_data.get('photo')
        if photo:
            instance.photo.delete()  # Удаление предыдущего фото
            instance.photo = photo
        instance.save()
        return instance

    def destroy(self, instance):
        # Удаление фото
        instance.photo.delete()
        instance.delete()


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         # model = UserData
#         model = User
#         fields = ["id", "email", "name", "password"]
#
#     def create(self, validated_data):
#         user = User.objects.create(email=validated_data['email'],
#                                        name=validated_data['name']
#                                        )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user


class PlayerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Player
        fields = '__all__'

    def create(self, validation_data):
        player = Player.objects.create(**validation_data)
        return player


class AgentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Agent
        fields = '__all__'

    def create(self, validation_data):
        agent = Agent.objects.create(**validation_data)
        return agent


class TrainerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Trainer
        fields = '__all__'

    def create(self, validation_data):
        trainer = Trainer.objects.create(**validation_data)
        return trainer


class ParentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Parent
        fields = '__all__'

    def create(self, validation_data):
        parent = Parent.objects.create(**validation_data)
        return parent


class ClubSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Club
        fields = '__all__'

    def create(self, validation_data):
        club = Club.objects.create(**validation_data)
        return club


class ScoutSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Scout
        fields = '__all__'

    def create(self, validation_data):
        scout = Scout.objects.create(**validation_data)
        return scout


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayersVideo
        fields = '__all__'

    def create(self, validation_data):
        video = PlayersVideo.objects.create(**validation_data)
        return video
