from django.urls import path
from . import views

urlpatterns = [
    path('wine', views.wine_list, name='wine_list'),
    path('gift', views.gift_list, name='gift_list'),
]