from django.http import JsonResponse


def SuccessJson(status=None, message=None, data=None, statusCode=None):
    return JsonResponse({
        "status": str(status),
        "message": str(message),
        "data": data,
        "status_code": str(statusCode)
    })
