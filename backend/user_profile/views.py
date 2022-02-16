from django.http import JsonResponse
from django.shortcuts import render
from utils.constants import SuccessJson


def UserProfile(request):
    return SuccessJson('success', 'user-profile', 'Profile data', '200')
