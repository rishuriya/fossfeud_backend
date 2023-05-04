from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
User=get_user_model()

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Registered
        fields='__all__'

class GamesSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Games
        fields='__all__'

class RoundsSerilizer(serializers.ModelSerializer):
    class Meta:
        model=gameRounds
        fields='__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class WinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model=winners
        fields='__all__'

class awardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Award
        fields='__all__'
