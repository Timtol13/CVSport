from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('registration', RegistrationAPIView)
router.register('login', LoginView)
router.register('advanced/Player', AdvancedRegistration_Player_ApiView)
router.register('advanced/Agent', AdvancedRegistration_Agent_ApiView)
router.register('advanced/Trainer', AdvancedRegistration_Trainer_ApiView)
router.register('advanced/Parent', AdvancedRegistration_Parent_ApiView)
router.register('advanced/Club', AdvancedRegistration_Club_ApiView)
router.register('advanced/Scout', AdvancedRegistration_Scout_ApiView)
router.register('add/video', AdvancedRegistration_Video_ApiView)

urlpatterns = [
    path('', include(router.urls)),
]
