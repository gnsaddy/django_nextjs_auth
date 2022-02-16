import json
from django.http import JsonResponse
from django.shortcuts import render


def ping_pong(request):
    return JsonResponse({"message": "ping-pong"})
