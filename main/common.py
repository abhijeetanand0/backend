from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK


def error_response(message):
    return Response({
        "result": "error",
        "message": message,
    }, status=HTTP_400_BAD_REQUEST)


def success_response(data):
    return Response({
        "result": "success",
        "data": data,
    }, status=HTTP_200_OK)
