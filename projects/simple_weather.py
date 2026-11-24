import requests

city = input("city name: ")

url = "https://geocoding-api.open-meteo.com/v1/search"
params = {"name":city, "count":1, "countryCode":"IR"}

try:
    data = requests.get(url, params=params).json()

    if "results" not in data:
        print("wtf city??")

    else:
        location = data["results"][0]
        lat = location["latitude"]
        lon = location["longitude"]

        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude":lat,
            "longitude":lon,
            "current":"temperature_2m,relative_humidity_2m"
        }

        weather = requests.get(url, params=params).json()
        current = weather["current"]

        print("city:", location["name"])
        print("temperature:", current["temperature_2m"], "C")
        print("humidity:", current["relative_humidity_2m"], "%")
except requests.exceptions.RequestException:
    print("errrrror")
#MadMad_34