from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('registration', RegistrationAPIView)
router.register('advanced/Player', AdvancedRegistration_Player_ApiView)

urlpatterns = [
    path('', include(router.urls)),
]