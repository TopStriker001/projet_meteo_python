import requests

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"


def get_coordinates(city):
    params = {"name": city, "count": 1, "language": "fr"}
    response = requests.get(GEOCODING_URL, params=params)
    data = response.json()
    result = data["results"][0]
    return result["latitude"], result["longitude"], result["name"]


def main():
    city = input("Ville : ")
    lat, lon, name = get_coordinates(city)
    print(f"{name} : {lat}, {lon}")


if __name__ == "__main__":
    main()