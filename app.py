import json

cities_path = "cities-example.json"

def get_cities_data(file):
    with open(file, "r", encoding="utf-8") as input:
        cities = json.load(input)
    return cities

cities = get_cities_data("cities-example.json")
print(cities)