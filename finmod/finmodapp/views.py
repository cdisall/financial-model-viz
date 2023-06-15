from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def index(request):
    return HttpResponse("This is our financial modeling app")

def api_endpoint_view(request):
    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {"function": "TIME_SERIES_DAILY", "symbol": "MSFT", "outputsize": "compact", "datatype": "json"}

    headers = {
        "X-RapidAPI-Key": "c08944d036msh3d8c9d791a92020p1a9db0jsn9585016e2aa8",
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    return HttpResponse(response)