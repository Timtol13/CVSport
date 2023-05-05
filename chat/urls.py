from django.urls import path

from .consumers import ChatConsumer

urlpatterns = [
    path("", ChatConsumer.as_asgi())
] 