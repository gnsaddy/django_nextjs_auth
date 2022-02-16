from django.urls import path

from user_profile import views

urlpatterns = [
    path('profile', views.UserProfile)
]
