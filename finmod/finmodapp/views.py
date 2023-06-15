from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def index(request):
    return HttpResponse("This is our financial modeling app")

def api_endpoint_view(request):
    url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/AAPL/financial-data"

    headers = {
        "X-RapidAPI-Key": "c08944d036msh3d8c9d791a92020p1a9db0jsn9585016e2aa8",
        "X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    return HttpResponse(response)