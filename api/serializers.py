from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name',  'email', 'facebook_user','telephone', 'profile', )

class UserRegistrationSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'confirm_password',)
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'confirm_password': {'write_only': True, 'required': True}
        }

    def create(self, validated_data):
        profile_data = validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        Profile.objects.create(user=user, **profile_data)

        return user


