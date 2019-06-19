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
    omdbUrl = "http://www.omdbapi.com/?apikey=" + settings.OMDB_API_KEY + "&t=" + request.GET['titleName']
    omdbResponse = requests.get(omdbUrl)
    return Response(status=status.HTTP_200_OK, data=omdbResponse.json())