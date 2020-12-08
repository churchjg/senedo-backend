from django.urls import path
from . import views

urlpatterns = [
    path('', views.wine_list, name='wine_list'),
]