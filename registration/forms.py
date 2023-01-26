from django.forms import ModelForm, PasswordInput, HiddenInput, TextInput, CharField
from django.contrib.auth.models import User
from . import models

class UserModelForm(ModelForm):
    class Meta:
        model = models.UserModel
        fields = ['role', 'first_name', 'second_name', 'patronimyc', 'age', 'shengen', 'weight', 'height', 
        'phone', 'email', 'country', 'city', 'description', 'is_show', 'subscribe', 'sources']
        widget = {
            'role': TextInput(attrs={'class': 'hidden'}),
        }
        

class PlayerForm(ModelForm):
    class Meta:
        model = models.Player
        fields = ['leg', 'position']

class AgentForm(ModelForm):
    class Meta:
        model = models.Agent
        fields = ['first_name', 'second_name', 'patronimyc']

class ParentForm(ModelForm):
    class Meta:
        model = models.Parent
        fields = ['first_name', 'second_name', 'patronimyc']

class ScoutForm(ModelForm):
    class Meta:
        model = models.Scout
        fields = ['first_name', 'second_name', 'patronimyc', 'school']

class ClubForm(ModelForm):
    class Meta:
        model = models.Club
        fields = ['first_name', 'second_name', 'patronimyc', 'school_ages']

class TrainerForm(ModelForm):
    class Meta:
        model = models.Trainer
        fields = ['first_name', 'second_name', 'patronimyc', 'country_s', 'city_s', 'phone_s', 'e_mail_s']

class DefUserForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['username', 'password']
        widget = {
            'username': TextInput(attrs={'class': 'form-control', 'name': 'username'}),
            'password': PasswordInput(attrs={'class': 'form-control', 'name': 'password'}),
        }

class LoginForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['username', 'password']
        widget = {
            'username': TextInput(attrs={'class': 'form-control', 'name': 'username'}),
            'password': PasswordInput(attrs={'class': 'form-control', 'name': 'password'}),
        }