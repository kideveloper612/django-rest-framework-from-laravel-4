from rest_framework import serializers
from snippets.models import Address
from django.contrib.auth.models import User


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Address
        fields = ['id', 'address_country', 'name', 'code']


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'id', 'username']
