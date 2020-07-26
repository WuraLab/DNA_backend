from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from .models import Profile,add_loan_record
from .serializers import   UserRegistrationSerializers, ProfileSerializer, EditProfileSerilizer,AddLoanSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated


# from rest_framework.parsers import FileUploadParser

#login was
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =  UserRegistrationSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    versions =['v1', 'v2','v3']
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
    versions = ['v1', 'v2', 'v3']
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


class AddLoanViewSet(viewsets.ModelViewSet):
    serializer_class = AddLoanSerializer
    queryset = add_loan_record.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)  #this option is used to authenticate a user, thus django can identify the token and its owner

    # only set permissions for actions as creating
     # pylint: disable=R0201
    def update(self, request, *args, **kwargs ):
        response = {'message': 'You cant Update your Profile like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
        # write a custom method that uses the authToken for access privileges


    






