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
    return Response(status=status.HTTP_200_OK, data=getTMdbTitle(request))

# TMdb API title 
def getTMdbTitle(request):
    # Individual title query
    if request.GET.get('titleName'):
        urlQuery = request.GET['titleName']
    # Multiple title query
    elif request.GET.get('query'):
        urlQuery = request.GET['query']
    # TODO: Pagination, language 
    tmdbUrl = "https://api.themoviedb.org/4/search/tv?query=" + urlQuery
    headers = {
        'Authorization' : settings.TMDb_ACCESS_TOKEN,
        'Content-Type' : 'application/json;charset=utf-8'
    }
    tmdbResponse = requests.get(tmdbUrl, headers=headers)
    return tmdbResponse.json()

# OMdb API title 
def getOMdbTitle(request):
    # Individual title query
    if request.GET.get('titleName'):
        urlQuery = "&t=" + request.GET['titleName']
    # Multiple title query
    elif request.GET.get('query'):
        urlQuery = "&s=" + request.GET['query']

    omdbUrl = "http://www.omdbapi.com/?apikey=" + settings.OMDB_API_KEY + urlQuery
    omdbResponse = requests.get(omdbUrl)
    return omdbResponse.json()