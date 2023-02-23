from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from API.views import RegisterView


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path(r'api/', include('API.urls')),
                  #path(r'add/',include('API.urls_photo')),
                  path('registration/',RegisterView.as_view(), name='registration'),
                  path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('login/verify/', TokenVerifyView.as_view(), name='token_verify'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
