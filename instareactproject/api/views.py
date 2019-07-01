import requests
import sys
from . import services
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(["GET"])
def title(request):
    """
    Returns list of titles
    """
    if not request.GET.get('query') and not request.GET.get('titleName'):
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Query not provided!'})

    rStatus, rData = status.HTTP_500_INTERNAL_SERVER_ERROR, None
    try:
        query = request.GET['query'] or request.GET['titleName']
        rData = services.getTMdbTitle(request, query)
        rStatus = status.HTTP_200_OK
    except requests.exceptions.RequestException as err:
        print(err)
        rStatus = status.HTTP_500_INTERNAL_SERVER_ERROR if status.is_server_error(err.response.status_code) else status.HTTP_400_BAD_REQUEST
        rData = {
            "page": 0,
            "total_results": 0,
            "total_pages": 0,
            "results": [],
            "message": err
        }
    return Response(status=rStatus, data=rData.json())

@api_view(["GET"])
def cast(request, titleId):
    """
    Returns list of cast members from a title
    """
    rStatus, rData = status.HTTP_500_INTERNAL_SERVER_ERROR, None
    res = services.getTMdbCast(request, titleId)
    if res.status_code == requests.codes['ok']:
        MAX_CAST_LOOKUP = 3
        rData = res.json()
        rStatus = res.status_code
        for i in range(MAX_CAST_LOOKUP):
            # TODO: Catch AJAX, check if valid name
            cxItem = services.getFirstCXUrl(rData['cast'][i]['name']).data
            rData['cast'][i]['item'] = cxItem
    return Response(status=rStatus, data=rData)
