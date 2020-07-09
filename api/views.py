# from rest_framework.response import Response
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from .models import Profile
from .serializers import   UserRegistrationSerializers
# from rest_framework.permissions import AllowAny, IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =  UserRegistrationSerializers