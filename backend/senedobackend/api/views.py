from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import Wine, Gift, Gallery, Event, Checkout, Home, Item
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, WineSerializer, GiftSerializer, GallerySerializer, EventSerializer, CheckoutSerializer, HomeSerializer, ItemSerializer
from flask import jsonify
from django.http import JsonResponse
from django.core import serializers




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

def wine_list(request):
    wines = Wine.objects.all()
    print(wines)
    wines_json = serializers.serialize("json", wines)
    return JsonResponse(wines_json, safe=False)

def gift_list(request):
    gifts = Gift.objects.all()
    print(gifts)
    gifts_json = serializers.serialize("json", gifts)
    return JsonResponse(gifts_json, safe=False)
    

def wine_detail(request, pk):
    wine = Wine.objects.get(id=pk)
    return render(request, 'vineyard/wine_detail.html', {'wine': wine})

def gift_detail(request, pk):
    gift = Gift.objects.get(id=pk)
    return render(request, 'vineyard/gift_detail.html', {'gift': gift})

def gallery_list(request):
    galleries = Gallery.objects.all()
    galleries_json = serializers.serialize("json", galleries)
    return JsonResponse(galleries_json, safe=False)

def gallery_detail(request, pk):
    gallery = Gallery.objects.get(id=pk)
    return render(request, 'vineyard/gallery_detail.html', {'gallery': gallery})

def event_list(request):
    events = Event.objects.all()
    events_json = serializers.serialize("json", events)
    return JsonResponse(events_json, safe=False)

def event_detail(request, pk):
    event = Event.objects.get(id=pk)
    return render(request, 'vineyard/event_detail.html', {'event': event})

def checkout_list(request):
    checkouts = Checkout.objects.all()
    checkouts_json = serializers.serialize("json", checkouts)
    return JsonResponse(checkouts_json, safe=False)

def checkout_detail(request, pk):
    checkout = Checkout.objects.get(id=pk)
    return render(request, 'vineyard/checkout_detail.html', {'checkout': checkout})

def home_list(request):
    homes = Home.objects.all()
    homes_json = serializers.serialize("json", homes)
    return JsonResponse(homes_json, safe=False)

def home_detail(request, pk):
    home = Home.objects.get(id=pk)
    return render(request, 'vineyard/home_detail.html', {'home': home})

def item_list(request):
    items = Item.objects.all()
    items_json = serializers.serialize("json", items)
    return JsonResponse(items_json, safe=False)

def item_detail(request, pk):
    item = item.objects.get(id=pk)
    return render(request, 'vineyard/item_detail.html', {'item': item})
    
