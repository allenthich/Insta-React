from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(["GET"])
def title(request):
    """
    Returns list of titles
    """
    titles = ["Terrace House:Aloha State","Breaking Bad"]
    return Response(status=status.HTTP_200_OK, data={"data": titles})