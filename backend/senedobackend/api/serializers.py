from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Wine, Gift

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class WineSerializer(serializers.HyperlinkedModelSerializer):
    Wine = serializers.HyperlinkedRelatedField(
        view_name='wine_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Wine
        fields = ('name', 'year', 'image', 'category', 'description', 'price', 'rating')

class GiftSerializer(serializers.HyperlinkedModelSerializer):
    Gift = serializers.HyperlinkedRelatedField(
        view_name='gift_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Gift
        fields = ('name', 'year', 'image', 'category', 'description', 'price')