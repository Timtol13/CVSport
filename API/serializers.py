from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user


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


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )
        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayersVideo
        fields = '__all__'

    def create(self, validation_data):
        video = PlayersVideo.objects.create(**validation_data)
        return video
