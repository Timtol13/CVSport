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
router.register('add/video', AdvancedRegistration_Video_ApiView)
#routerS = SimpleRouter()
#routerS.register('user_photos', UserPhotoApiView, basename='userphoto')
urlpatterns = [
    path('', include(router.urls)),
    path('add/photo/<str:username>/', UserPhotoApiView.as_view({'get': 'retrieve','put':'update','delete':'destroy','post':'create'})),
    #path('advanced/Player/<str:username>/', AdvancedRegistration_Player_ApiView.as_view({'put': 'update_username', 'delete':'destroy'}), name='player-detail')
]
#urlpatterns += routerS.urls
