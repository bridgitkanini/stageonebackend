from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
import requests

def hello(request):
    visitor_name = request.GET.get('visitor_name', 'Visitor')
    client_ip = request.META.get('REMOTE_ADDR', '127.0.0.1')

    # Get location information
    ip_info = requests.get(f'http://ip-api.com/json/{client_ip}').json()
    location = ip_info.get('city', 'Unknown Location')
    temperature = 11  # Static temperature for the example

    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}"

    return JsonResponse({
        "client_ip": client_ip,
        "location": location,
        "greeting": greeting
    })

