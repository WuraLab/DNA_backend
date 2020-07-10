from rest_framework.response import Response
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from .models import Profile
from .serializers import   UserRegistrationSerializers, ProfileSerializer, EditProfileSerilizer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import FileUploadParser

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =  UserRegistrationSerializers

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = (TokenAuthentication,)  #this option is used to authenticate a user, thus django can identify the token and its owner
    permission_classes = (IsAuthenticated,)
    parser_class = (FileUploadParser,)


    # only set permissions for actions as update
    # remember to customise Create, delete, retreive

    @action(detail=True, methods=['POST'] )
    def update_profile(self, request, pk=None,):


        if request.data :
            fetched_data =  request.data
            user = request.user

            try :
                 profile = Profile.objects.filter(user=user.id, id=pk )
                 # profile.update(**fetched_data)
                 profile.update(facebook_user=fetched_data['facebook_user'],
                                phone=fetched_data['phone'],
                                profile=request.FILES.get('profile'))
                 serializer = EditProfileSerilizer(profile, many=False)
                 response = {'message': 'User profile  Updated', 'result': serializer.data}
                 return Response(response, status=status.HTTP_200_OK)

            except IndexError :
                response = {'message': 'user profile does not exit'}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'Nothing to update!'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)