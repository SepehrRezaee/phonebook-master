from rest_framework import serializers

from phones.models import Entry


class EntrySerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Entry
        fields = [
            'pk',
            'username',
            'first_name',
            'last_name',
            'phone_number',
        ]
