from django.urls import path
from .views import *

urlpatterns = [
    path("users", MyUserListApi.as_view(), name="Users"),
    path("my_messages", MyMessagesList.as_view(), name="my-message"),
]
