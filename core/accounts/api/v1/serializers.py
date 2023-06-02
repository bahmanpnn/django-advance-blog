from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

#thirdparty
from rest_framework import serializers

from rest_framework import serializers
#project
from ...models import User


class RegistrationSerializer(serializers.ModelSerializer):

    # password1=serializers.CharField(max_length=255,write_only=True)
    password_one=serializers.CharField()

    class Meta:
        model=User
        fields=['email','password','password_one']

    def validate(self, attrs):

        #this condition is for checking password and second password is equal or not!
        if attrs.get('password') != attrs.get('password_one'):
            raise serializers.ValidationError({'detail':'passwords does not match!!'})
        
        #try except is for checking password complexity
        try:
            validate_password(attrs.get('password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'password':list(e.messages)})

        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop('password_one',None)
        return User.objects.create_user(**validated_data)
    
    
class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get('email')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

