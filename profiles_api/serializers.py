from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer):

    """Serializers a name field for testin our apiview"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:  #when modelserializer is used we use class meta
        model=models.UserProfile
        fields=('id','email','name','password')
        extra_kwargs={
        'password':{
            'write_only':True,    #only to update not to retrieve
            'style':{'input_type':'password'}
        }
        }

    def create(self,validated_data):
        """create and return a new user"""
        user = models.UserProfile.objects.create_user(
           email = validated_data['email'],
           name = validated_data['name'],
           password= validated_data['password']
        )

        return user
