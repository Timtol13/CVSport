from django.urls import path, include

from registration.views import RegisterView

urlpatterns = [
    path('', RegisterView.as_view(), name='registration'),
    # path('login', LoginAPIView.as_view(), name='registration'),

]