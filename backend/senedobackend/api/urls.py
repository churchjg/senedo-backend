from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.wine_list, name='wine_list'),
    path('wine', views.wine_list, name='wine_list'),
    path('gift', views.gift_list, name='gift_list'),
    path('gallery', views.gallery_list, name='gallery_list'),
    path('event', views.event_list, name='event_list'),
    path('checkout', views.checkout_list, name='checkout_list'),
]