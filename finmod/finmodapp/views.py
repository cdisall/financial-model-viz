from django.shortcuts import render
from django.http import HttpResponse
import requests
import matplotlib.pyplot as plt
import io
import base64
import datetime
import json
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer

# Create your views here.

# this view shows a singular stock time series for MSFT
def api_endpoint_view(request):
    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {"interval": "5min", "function": "TIME_SERIES_INTRADAY", "symbol": "MSFT", "datatype": "json",
                   "output_size": "compact"}

    headers = {
        "X-RapidAPI-Key": "c08944d036msh3d8c9d791a92020p1a9db0jsn9585016e2aa8",
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    # return(HttpResponse(response))

    # Load data from JSON string
    data = response.json()['Time Series (5min)']

    # Extract timestamps and opening prices from the data
    timestamps = []
    opening_prices = []
    for timestamp, entry in data.items():
        timestamps.append(datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"))
        opening_prices.append(float(entry['1. open']))

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, opening_prices)
    plt.xlabel("Time")
    plt.ylabel("Opening Price")
    plt.title("Opening Price Over Time")
    plt.xticks(rotation=45)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    httpResponse = HttpResponse(content_type='image/png')
    httpResponse.write(buffer.getvalue())
    return httpResponse

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]