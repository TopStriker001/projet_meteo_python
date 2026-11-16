import requests

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def get_coordinates(city):
    params = {"name": city, "count": 1, "language": "fr"}
    response = requests.get(GEOCODING_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    if "results" not in data:
        raise ValueError(f"Ville introuvable : « {city} »")

    result = data["results"][0]
    return result["latitude"], result["longitude"], result["name"]

def get_weather(lat, lon):
    """Récupère la température et le vent actuels."""
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m",
    }
    response = requests.get(WEATHER_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()["current"]

def display_weather(name, weather):
    """Affiche la météo de façon lisible."""
    print("\n" + "=" * 30)
    print(f"  Météo à {name}")
    print("=" * 30)
    print(f"  Température : {weather['temperature_2m']} °C")
    print(f"  Vent        : {weather['wind_speed_10m']} km/h")
    print("=" * 30 + "\n")

def ask_city():
    """Demande une ville jusqu'à en trouver une valide (q pour quitter)."""
    while True:
        city = input("Ville (q pour quitter) : ").strip()
        if city.lower() == "q":
            return None
        if not city:
            print("Tu n'as pas saisi de ville, réessaie.")
            continue
        try:
            return get_coordinates(city)
        except ValueError as e:
            print(f"Erreur : {e}. Réessaie.")


def main():
    try:
        result = ask_city()
        if result is None:
            return
        lat, lon, name = result
        weather = get_weather(lat, lon)
        display_weather(name, weather)
    except requests.exceptions.ConnectionError:
        print("Erreur : pas de connexion internet.")
    except requests.exceptions.Timeout:
        print("Erreur : le serveur met trop de temps à répondre.")
    except requests.exceptions.RequestException as e:
        print(f"Erreur réseau : {e}")

if __name__ == "__main__":
    main()