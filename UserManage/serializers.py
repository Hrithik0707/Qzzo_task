from rest_framework import serializers
from .models import User
import random
import string
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','unique_id', 'age','image', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        if validated_data['unique_id']==None:
            sample_str = ''.join((random.choice(string.ascii_letters) for i in range(3)))
            sample_str += ''.join((random.choice(string.digits) for i in range(3)))
            sample_list = list(sample_str)
            random.shuffle(sample_list)
            final_string = ''.join(sample_list)
            user.unique_id = final_string
        user.set_password(validated_data['password'])
        user.save()
        return user


# class LoginSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(
#         max_length=65, min_length=8, write_only=True)
#     email = serializers.CharField(max_length=254)

#     class Meta:
#         model = User
#         fields = ['email', 'password']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        max_length=100,
        style={'placeholder': 'Email', 'autofocus': True}
    )
    password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    