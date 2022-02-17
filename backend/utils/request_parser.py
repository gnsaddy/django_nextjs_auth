from functools import wraps
from urllib import request

from django.http import JsonResponse

from utils.utils_functions import json_required, missing_json_fields, wrong_data_type, wrong_length


def required_params(required):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            _json = request.get_json()
            if _json is None:
                response = json_required()
                return JsonResponse(response), 400

            missing = [r for r in required.keys()
                       if r not in _json]

            if missing:
                response = missing_json_fields(missing)
                return JsonResponse(response), 400
            wrong_types = [r for r in required.keys()
                           if not isinstance(_json[r], required[r])]

            if wrong_types:
                response = wrong_data_type(wrong_types)
                return JsonResponse(response), 400

            length_error = [r for r in required.keys() if isinstance(
                _json[r], str) and not len(_json[r])]

            if length_error:
                response = wrong_length(length_error)
                return JsonResponse(response), 400

            return fn(*args, **kwargs)

        return wrapper

    return decorator
