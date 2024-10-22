from django.urls import path
from rest_framework.routers import DefaultRouter

from account import views
from single_device.views import DeviceViewSet

router=DefaultRouter()
router.register('login', DeviceViewSet, basename='login')
urlpatterns =router.urls
