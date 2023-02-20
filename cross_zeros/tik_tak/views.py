from django.db.models import Q

# Create your views here.
from rest_framework import generics
from .models import MyUser, Message
from .serializers import MessageSerializer, MyUserSerializer


class MyUserListApi(generics.ListAPIView):
    """
    All users profiles
    """

    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class MyMessagesList(generics.ListAPIView):
    """
    Messages of current user
    """

    def get_queryset(self):
        return Message.objects.filter(
            Q(from_user=self.request.user) | Q(to_user=self.request.user)
        )

    serializer_class = MessageSerializer
