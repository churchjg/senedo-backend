from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Wine, Gift, Gallery, Event, Checkout

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

class GallerySerializer(serializers.HyperlinkedModelSerializer):
    Gallery = serializers.HyperlinkedRelatedField(
        view_name='gallery_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Gallery
        fields = ('name', 'image', 'description')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    Event = serializers.HyperlinkedRelatedField(
        view_name='event_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Event
        fields = ('name', 'image', 'date', 'description')

class CheckoutSerializer(serializers.HyperlinkedModelSerializer):
    Checkout = serializers.HyperlinkedRelatedField(
        view_name='checkout_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Checkout
        fields = ('first', 'last', 'address1', 'address2', 'city', 'state', 'zip', 'country', 'cardname', 'cardnumber', 'expiration', 'cvv')