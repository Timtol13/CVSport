from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.Registration),
    path('login', views.Login),
    path('advance/<slug:user>/<slug:role>', views.Advance),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)