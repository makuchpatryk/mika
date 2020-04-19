import json

from django.http import request, Http404, HttpResponse
from django.utils.datastructures import MultiValueDict

def to_query_dict(data):
    """Converts dict or QueryDict into QueryDict-like objet
    """
    tmp = MultiValueDict()

    if isinstance(data, request.QueryDict):
        for key in data.keys():
            tmp.setlist(key.rstrip('[]'), data.getlist(key))
        return tmp
    elif isinstance(data, dict):
        # Imagine you have following data:
        # images = [1,2,3]
        # jQuery when encoding such information will build
        # &images[]=1&images[]=2&images[]=3, this is in line with
        # specification, however some user may send request like that
        # &images=1&images=2&images=3, not sure if it's true to spec but for
        # sure works in majority of web frameworks
        for key, value in data.items():

            if isinstance(value, list):
                tmp.setlist(key.rstrip('[]'), value)
            else:
                tmp[key.rstrip('[]')] = value

        return tmp
    else:
        raise ValueError("No idea how to convert that")


def api_res(body=None, status=400, request=None):
    response = HttpResponse()
    response.status_code = status
    if body:
        response.content = json.dumps(body)

    response["Access-Control-Allow-Headers"] = "Accept, Origin, Content-Type, Authorization"
    response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, DELETE"
    response["Access-Control-Allow-Origin"] = "http://localhost:8080"
    response["Content-Type"] = 'application/json'

    if request and request.path_info:
        url = str(request.path_info)

        if url.startswith('/api-biz'):
            response["Access-Control-Allow-Origin"] = "http://localhost"

        if url.startswith('/api-biz-ios'):
            response["Access-Control-Allow-Origin"] = "capacitor://localhost"


    return response
