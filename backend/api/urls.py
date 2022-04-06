from django.urls import path, include
from .views import ping_pong

urlpatterns = [
    path('ping/', ping_pong),
    path('auth/', include('api.auth_api.urls')),
]
