from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from .models import Profile
from .serializers import   UserRegistrationSerializers, ProfileSerializer, EditProfileSerilizer
from rest_framework.permissions import AllowAny, IsAuthenticated
import jwt
import os
from datetime import datetime, timedelta
# favour django-mailer but fall back to django.core.mail
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


# from rest_framework.parsers import FileUploadParser

#login was
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =  UserRegistrationSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    versions =['v1']
    # update - default method should be restricted
    # pylint: disable=R0201
    def update(self, request, *args, **kwargs ):
        response = {'message': 'You cant Update your Profile like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # destroy - IsAuthenticated an isSelf
    # pylint: disable=R0201
    def destroy(self, request,  *args, **kwargs):
        response = {'message': 'You cant delete Profile like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # retrieve - default method for all should be restricted,
    # pylint: disable=R0201
    def list(self, request, *args, **kwargs):
        response = {'message': 'You cant  list or retrieve users Profile like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    # pylint: disable=R0201
    def retrieve(self, request, pk=None, *args, **kwargs):
        response = {'message': 'You cant  list or retrieve users Profile like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = (TokenAuthentication,)  #this option is used to authenticate a user, thus django can identify the token and its owner
    permission_classes = (IsAuthenticated,)
    versions = ['v1']
    # only set permissions for actions as update
    # remember to customise Create, delete, retrieve

    # pylint: disable=R0201
    def update(self, request, *args, **kwargs):
        response = {'message': 'You cant edit your Profile like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # pylint: disable=R0201
    def create(self, request, *args, **kwargs):
        response = {'message': 'You cant create Profile like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # pylint: disable=R0201
    def destroy(self, request,  *args, **kwargs):
        response = {'message': 'You cant delete Profile like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # pylint: disable=R0201
    def list(self, request, version="v1", *args, **kwargs):
            # check if the version argument exists in the versions list
         if version in self.versions:

                if request.user:
                    try:
                        user = request.user
                        profile = Profile.objects.get(user=user.id)
                        serializer = ProfileSerializer(profile, many=False)
                        response = {'message': 'User profile ', 'result': serializer.data}
                        return Response(response, status=status.HTTP_200_OK)
                    except IndexError:
                        response = {'message': 'User not Authenticated! '}
                        return Response(response, status=status.HTTP_400_BAD_REQUEST)

         else:
            response = {'message': 'API version not identified!'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


    # pylint: disable=R0201
    def retrieve(self, request, pk=None,  *args, **kwargs):
        response = {'message': 'You cant retrieve users Profile like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


    # write a custom method that uses the authToken for access privileges
    # pylint: disable=R0201
    @action(detail=True, methods=['PUT'])
    def update_profile(self, request, version="v1", pk=None,):
        # check if the version argument exists in the versions list
        if version in self.versions:
            if request.data :
                fetched_data =  request.data
                user = request.user
                try :
                     profile = Profile.objects.filter(user=user.id, id=pk )
                     profile.update(facebook_user=fetched_data['facebook_user'],
                                    phone=fetched_data['phone'],
                                    profile=request.FILES.get('profile'))
                     get_profile = Profile.objects.get(user=user.id, id=pk)
                     serializer = EditProfileSerilizer(get_profile, many=False)
                     response = {'message': 'User profile  Updated', 'result': serializer.data}
                     return Response(response, status=status.HTTP_200_OK)

                except IndexError :
                    response = {'message': 'user profile does not exit'}
                    return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'API version not identified!'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
class RecoveryViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all() #used by serializers output
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    versions =['v1']

    def update(self, request, *args, **kwargs):
        response = {'message': 'You cant edit your Profile like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

     # pylint: disable=R0201
    def list(self, request, *args, **kwargs):
        response = {'message': 'You cant create Profile like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

     # pylint: disable=R0201
    def destroy(self, request,  *args, **kwargs):
        response = {'message': 'You cant delete Profile like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # pylint: disable=R0201
    def retrieve(self, request, pk=None,  *args, **kwargs):
        response = {'message': 'You cant retrieve users Profile like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


    def create(self, request, version="v1", *args, **kwargs):
    # check if the version argument exists in the versions list
        if version in self.versions:
            if request.data :
                fetched_data =  request.data
                email= fetched_data['email']
                try :
                #    check in fetch email exits
                    user = User.objects.get(email=email)
                    # create jwt token
                    secret = os.getenv("JWTSECRET")
                    # token expires in 30 seconds
                    # minutes=1
                    dt = datetime.now() + timedelta(minutes=30)   
                    encoded = jwt.encode({'email': email, 'exp': dt}, secret ,  algorithm='HS256')
                    reset_link = f'{os.getenv("RESETPASS_URL")}/{encoded.decode("utf-8")}'

                    # send an e-mail to the user
                    context = {
                         'user': user,
                         'reset_link': reset_link
                    }
                    
                    msg_plain = render_to_string('../templates/password_reset_email.txt', context)
                    msg_html = render_to_string('../templates/password_reset_email.html', context)

                    subject = 'Debt notification account recovery request.'
                    from_email = settings.EMAIL_HOST_USER
                    message = msg_plain
                    recipient_list = [email]

                    send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=msg_html)

                    response= {'token': 'email sent!'}
                    return Response(response, status=status.HTTP_200_OK)
                except User.DoesNotExist:
                    response = {'message': 'No user associated with this email exits!'}
                    return Response(response, status=status.HTTP_404_NOT_FOUND)
        else:
            response = {'message': 'API version not identified!'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST'])
    def validate_token(self,request, version="v1"):
        if version in self.versions:
            if request.data :
                fetched_data =request.data
                encoded_token= fetched_data['token']
                try:
                        secret = os.getenv("JWTSECRET")
                        decode_token = jwt.decode(encoded_token, secret,  leeway=10, algorithms=['HS256'])
                        response= {'message': 'Token is still valid and active :)'}
                        return Response(response, status=status.HTTP_200_OK)
                except jwt.ExpiredSignatureError:
                        response= {'message': 'Token expired. Get new one'}
                        return Response(response, status=status.HTTP_200_OK)
                except jwt.InvalidTokenError:
                        response= {'message': 'Invalid Token'}
                        return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'API version not identified!'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST) 
    
    @action(detail=False, methods=['POST'])
    def confirm(self,request, version="v1"):
        if version in self.versions:
            if request.data :
                try:
                    # user token and password
                    fetched_data =request.data
                    encoded_token= fetched_data['token']
                    new_password = fetched_data['password']

                    secret = os.getenv("JWTSECRET")
                    decode_token = jwt.decode(encoded_token, secret,  leeway=10, algorithms=['HS256'])
                    email = decode_token['email']
                   
                    # modify existing user
                    user = User.objects.get(email=email)
    
                    user.set_password(new_password)
                    user.save()
                    response = {'success': 'Password reset was successful!'}
                    return Response(response, status=status.HTTP_200_OK)

                except jwt.InvalidTokenError:
                    response= {'message': 'Invalid Token'}
                    return Response(response, status=status.HTTP_200_OK)
                except User.DoesNotExist:
                    response = {'message': 'No user associated with this email exits!'}
                    return Response(response, status=status.HTTP_200_OK)
                   
                    response = {'message': 'API version not identified!'}
                    return Response(response, status=status.HTTP_400_BAD_REQUEST) 

        else:
            response = {'message': 'API version not identified!'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST) 