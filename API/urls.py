from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

router = DefaultRouter()

# router.register('registration', RegistrationAPIView.as_view())
# router.register('login', LoginView),

router.register('advanced/Player', AdvancedRegistration_Player_ApiView)
router.register('advanced/Agent', AdvancedRegistration_Agent_ApiView)
router.register('advanced/Trainer', AdvancedRegistration_Trainer_ApiView)
router.register('advanced/Parent', AdvancedRegistration_Parent_ApiView)
router.register('advanced/Club', AdvancedRegistration_Club_ApiView)
router.register('advanced/Scout', AdvancedRegistration_Scout_ApiView)
# router.register('add/video', AdvancedRegistration_Video_ApiView)
urlpatterns = [
    path('', include(router.urls)),
    path('add/photo/', UserPhotoApiView.as_view({'get': 'list'}), name='user-photo-list'),
    path('add/photo/<str:username>/',
         UserPhotoApiView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'post': 'create'}),
         name='user-photo'),
    path('add/video/', AdvancedRegistration_Video_ApiView.as_view({'get': 'list'}), name='user-video-list'),
    path('add/video/<str:username>/',
         AdvancedRegistration_Video_ApiView.as_view(
             {'get': 'retrieve', 'put': 'update', 'post': 'create','delete': 'destroy'}),
         name='user-video'),
    path('add/video/<str:username>/<int:pk>/',
         AdvancedRegistration_Video_ApiView.as_view(
             {'delete': 'destroy'}),
         name='user-video'),
    path('advanced/Player/<str:username>/',
         AdvancedRegistration_Player_ApiView.as_view({'put': 'update_username', 'delete': 'destroy'}),
         name='player-detail'),
    path('advanced/Agent/<str:username>/',
         AdvancedRegistration_Agent_ApiView.as_view({'put': 'update_username', 'delete': 'destroy'}),
         name='agent-detail'),
    path('advanced/Parent/<str:username>/',
         AdvancedRegistration_Parent_ApiView.as_view({'put': 'update_username', 'delete': 'destroy'}),
         name='parent-detail'),
    path('advanced/Club/<str:username>/',
         AdvancedRegistration_Club_ApiView.as_view({'put': 'update_username', 'delete': 'destroy'}),
         name='club-detail'),
    path('advanced/Scout/<str:username>/',
         AdvancedRegistration_Scout_ApiView.as_view({'put': 'update_username', 'delete': 'destroy'}),
         name='scout-detail'),
    path('advanced/Trainer/<str:username>/',
         AdvancedRegistration_Trainer_ApiView.as_view({'put': 'update_username', 'delete': 'destroy'}),
         name='trainer-detail')
]
# urlpatterns += routerS.urls
