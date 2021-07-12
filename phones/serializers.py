from django.contrib.auth.models import User, Group
from rest_framework import serializers

from phones.models import Entry

"""
Admin serializers
"""


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


"""
Models serializer
"""


class EntrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Entry
        field = [
            'id',
            'first_name',
            'last_name',
            'phone_number',
        ]
