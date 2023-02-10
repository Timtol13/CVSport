from rest_framework import serializers
from .models import *
from API.models import UserData


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'password']
#
#         extra_kwargs = {
#             'password': {
#                 'write_only': True,
#                 'required': True
#             }
#         }
#
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
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
