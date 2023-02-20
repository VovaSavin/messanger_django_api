from rest_framework import serializers
from .models import MyUser, Message


class MyUserSerializer(serializers.ModelSerializer):
    """
    To json MyUser
    """

    class Meta:
        model = MyUser
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    """
    To json Message
    """

    class Meta:
        model = Message
        fields = "__all__"
