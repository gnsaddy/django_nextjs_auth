
from django.urls import path
from .views import auth_ping

urlpatterns = [
    path('auth-ping/', auth_ping)
]
