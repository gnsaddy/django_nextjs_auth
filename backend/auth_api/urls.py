from django.urls import path

from auth_api import views

urlpatterns = [
    path('ping/', views.ping_pong)
]
