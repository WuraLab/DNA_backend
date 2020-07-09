from rest_framework.response import Response
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from .models import Profile
from .serializers import   UserRegistrationSerializers, ProfileSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =  UserRegistrationSerializers

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = (TokenAuthentication,)  #this option is used to authenticate a user, thus django can identify the token and its owner
    permission_classes = (AllowAny,)

    # only set permissions for actions as update
    # remember to customise Create, delete, retreive