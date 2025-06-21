import json
import requests
import pandas as pd
import xml.etree.ElementTree as ET
import sys

def get_data_from_cities():
    file = "cities-example.json"
    with open(file, "r", encoding="utf-8") as input:
        data = json.load(input)
        return data

def get_forecast(lat, lon):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/classic?lat={lat}&lon={lon}"
    

cities = get_data_from_cities()
data = get_forecast(59.9139, 10.7522)
print(cities)