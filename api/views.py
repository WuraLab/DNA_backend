from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Payu.models import RegistrationModel
from rest_framework.views import APIView


from api.serializers import  RegisterSerializer
from rest_framework import generics
from rest_framework import status, viewsets
from rest_framework import mixins


from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


from .googleviews import GoogleOAuth2AdapterIdToken

from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response














class NameRegistrationView(generics.ListCreateAPIView):
    queryset = RegistrationModel.objects.all()
    serializer_class = RegisterSerializer

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


 # import custom adapter
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2AdapterIdToken
    client_class = OAuth2Client