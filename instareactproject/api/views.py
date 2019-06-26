import requests
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from instareactproject import settings

TMDB_HEADERS = {
    'Authorization' : settings.TMDb_ACCESS_TOKEN,
    'Content-Type' : 'application/json;charset=utf-8'
}

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
    tmdbResponse = requests.get(tmdbUrl, headers=TMDB_HEADERS)
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

@api_view(["GET"])
def cast(request, titleId):
    """
    Returns list of cast members from a title
    """
    tmdbUrl = "https://api.themoviedb.org/3/tv/" + titleId + "/credits?api_key=" + settings.TMDb_API_KEY
    tmdbResponse = requests.get(tmdbUrl, headers=TMDB_HEADERS)
    
    if tmdbResponse.status_code == requests.codes.ok:
        return Response(status=status.HTTP_200_OK, data=tmdbResponse.json())
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)