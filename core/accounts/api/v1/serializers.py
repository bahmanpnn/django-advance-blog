from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
#thirdparty
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