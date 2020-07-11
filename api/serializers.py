from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import obtain_auth_token


class UserRegistrationSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }

    def create(self, validated_data):
        profile_data = validated_data
        user = User.objects.create_user(**profile_data)
        Token.objects.create(user=user)
        Profile.objects.create(user=user)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    user = UserRegistrationSerializers()
    token = obtain_auth_token
    class Meta:
        model = Profile
        fields = ('id',  'facebook_user','phone', 'profile', 'user' )

class EditProfileSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'facebook_user', 'phone', 'profile',  )