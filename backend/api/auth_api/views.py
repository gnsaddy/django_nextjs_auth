from ..utils.constants import SuccessJson


def auth_ping(request):
    return SuccessJson('success', 'ping from auth api', 'auth api', 200)
