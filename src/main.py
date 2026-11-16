import requests

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def get_coordinates(city):
    params = {"name": city, "count": 1, "language": "fr"}
    response = requests.get(GEOCODING_URL, params=params)
    data = response.json()
    result = data["results"][0]
    return result["latitude"], result["longitude"], result["name"]

def get_weather(lat, lon):
    """Récupère la température et le vent actuels."""
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m",
    }
    response = requests.get(WEATHER_URL, params=params)
    return response.json()["current"]


def display_weather(name, weather):
    """Affiche la météo de façon lisible."""
    print("\n" + "=" * 30)
    print(f"  Météo à {name}")
    print("=" * 30)
    print(f"  Température : {weather['temperature_2m']} °C")
    print(f"  Vent        : {weather['wind_speed_10m']} km/h")
    print("=" * 30 + "\n")


def main():
    city = input("Ville : ")
    lat, lon, name = get_coordinates(city)
    weather = get_weather(lat, lon)
    display_weather(name, weather)

if __name__ == "__main__":
    main()