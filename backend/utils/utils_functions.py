import json


def json_required():
    response = {
        "status": 400,
        "message": "This API Expects parameter. Passed None"
    }

    return response


def missing_json_fields(missing):
    response = {
        "status": 400,
        "message": f'Request data for {missing} is/are missing some required params',
        "missing": {
            "error": missing,
            "type": "Required fields"
        }
    }
    return response, 400


def wrong_data_type(wrong_types):
    response = {
        "status": 400,
        "message": f"Data types in the request data {wrong_types} doesn't match the required format",
        "param_types": {
            "error": wrong_types,
            "type": "Data type mismatch"
        }
    }

    return response, 400


def wrong_length(length_error):
    response = {
        "status": 400,
        "message": f"Parameter of the requested data {length_error} is empty",
        "param_types": {
            "error": length_error,
            "type": "Missing parameter"
        }
    }

    return response, 400
