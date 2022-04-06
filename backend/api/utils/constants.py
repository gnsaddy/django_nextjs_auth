from django.http import JsonResponse


class JsonConstants:
    status = 'status'
    message = 'message'
    data = 'data'
    statusCode = 'statusCode'
    success = 'success'
    error = 'error'
    contentType = 'content-type'
    applicationJson = 'application/json'


def SuccessJson(status=None, message=None, data=None, statusCode=None):
    return JsonResponse({
        "status": str(status),
        "message": str(message),
        "data": data,
        "status_code": int(statusCode)
    })


def ErrorJson(status=None, message=None, data=None, statuscode=None):
    return JsonResponse({
        "status": str(status),
        "message": str(message),
        "data": data,
        "status_code": int(statuscode)
    })
