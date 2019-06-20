import requests
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from instareactproject import settings

@api_view(["GET"])
def title(request):
    """
    Returns list of titles
    """
    urlQuery = ""
    # Individual title query
    if request.GET.get('titleName'):
        urlQuery = "&t=" + request.GET['titleName']
    # Multiple title query
    elif request.GET.get('search'):
        urlQuery = "&s=" + request.GET['search']

    omdbUrl = "http://www.omdbapi.com/?apikey=" + settings.OMDB_API_KEY + urlQuery
    omdbResponse = requests.get(omdbUrl)
    return Response(status=status.HTTP_200_OK, data=omdbResponse.json())