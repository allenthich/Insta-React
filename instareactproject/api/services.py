import requests
import time
from instareactproject import settings
from rest_framework.response import Response
from rest_framework import status

MAX_RETRIES = 3
TMDB_HEADERS = {
    'Authorization' : settings.TMDb_ACCESS_TOKEN,
    'Content-Type' : 'application/json;charset=utf-8'
}

def makeRequest(url, headers={}):
    numAttempts = 0
    res = None
    while numAttempts < MAX_RETRIES:
        res = requests.get(url, headers=headers, timeout=10)
        if res.ok:
            break
        else:
            numAttempts += 1
            time.sleep(3)          
    res.raise_for_status()
    return res

# TMdb API title 
def getTMdbTitle(request, query):
    # TODO: Pagination, language 
    tmdbUrl = "https://api.themoviedb.org/4/search/tv?query=" + query
    return makeRequest(tmdbUrl, TMDB_HEADERS)

# TMdb API Cast
def getTMdbCast(request, titleId):
    tmdbUrl = "https://api.themoviedb.org/3/tv/" + titleId + "/credits?api_key=" + settings.TMDb_API_KEY
    return makeRequest(tmdbUrl, TMDB_HEADERS)

# TMdb API Person
def getTMdbPerson(memberId):
    """
    Retrieve person info. from TMdb
    """
    return memberId

# Google Custom Search API
def getFirstCXUrl(query):
    """
    Retrieves first URL from Google Custom Search API
    """
    GOOGL_CX_API = "https://www.googleapis.com/customsearch/v1?key=" + settings.GOOGLE_CX_API_KEY + "&cx=" + settings.GOOGLE_CX_ENGINE_ID
    googleCxUrl = GOOGL_CX_API + "&q=" + query
    googleCxResponse = makeRequest(googleCxUrl)

    rStatus, rData = status.HTTP_500_INTERNAL_SERVER_ERROR, None
    if googleCxResponse.status_code == requests.codes['ok']:
        rStatus = status.HTTP_200_OK
        rData = googleCxResponse.json()['items'][0] or {}
    return Response(status=rStatus, data=rData)

# Utility/Helper Functions
def isValidName(nameStr):
    """
    Returns bool whether name consists of first and last
    """
    return len(nameStr.split(' ')) >= 1

def getTMdbAlias(memberId):
    """
    Retrieve additional alias from TMdb
    """
    return memberId
        