from django.urls import path
from . import views

urlpatterns = [
    path('', views.wine_list, name='wine_list'),
    path('gift', views.gift_list, name='gift_list'),
    path('gallery', views.gift_list, name='gallery_list'),
]