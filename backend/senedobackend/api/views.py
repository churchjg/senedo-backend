from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import Wine, Gift, Gallery
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer

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
    return render(request, 'vineyard/wine_list.html', {'wines': wines})

def gift_list(request):
    gifts = Gift.objects.all()
    return render(request, 'vineyard/gift_list.html', {'gifts': gifts})

def wine_detail(request, pk):
    wine = Wine.objects.get(id=pk)
    return render(request, 'vineyard/wine_detail.html', {'wine': wine})

def gift_detail(request, pk):
    gift = Gift.objects.get(id=pk)
    return render(request, 'vineyard/gift_detail.html', {'gift': gift})

def gallery_list(request):
    galleries = Gallery.objects.all()
    return render(request, 'vineyard/gallery_list.html', {'galleries': galleries})

def gallery_detail(request, pk):
    gallery = Gallery.objects.get(id=pk)
    return render(request, 'vineyard/gallery_detail.html', {'gallery': gallery})
