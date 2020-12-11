"""senedobackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers
from senedobackend.api import views
from django.conf.urls import include
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Setup automatic URL routing
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('router', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #api routing
    path('admin', admin.site.urls),
    path('', include('senedobackend.api.urls')),
    path('wines/<int:pk>', views.wine_detail, name='wine_detail'),
    path('gifts/<int:pk>', views.gift_detail, name='gift_detail'),
    path('galleries/<int:pk>', views.gallery_detail, name='gallery_detail'),
    path('events/<int:pk>', views.event_detail, name='event_detail'),
]
