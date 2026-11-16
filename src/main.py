import requests

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

WEATHER_CODES = {
    0: "Ciel dégagé",
    1: "Plutôt dégagé",
    2: "Partiellement nuageux",
    3: "Couvert",
    45: "Brouillard",
    48: "Brouillard givrant",
    51: "Bruine légère",
    53: "Bruine",
    55: "Bruine forte",
    61: "Pluie légère",
    63: "Pluie",
    65: "Pluie forte",
    71: "Neige légère",
    73: "Neige",
    75: "Neige forte",
    80: "Averses légères",
    81: "Averses",
    82: "Averses violentes",
    95: "Orage",
    96: "Orage avec grêle",
    99: "Orage violent avec grêle",
}


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
        "current": (
            "temperature_2m,apparent_temperature,relative_humidity_2m,"
            "precipitation,wind_speed_10m,weather_code"
        ),
    }
    response = requests.get(WEATHER_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()["current"]

def display_weather(name, weather):
    """Affiche la météo de façon lisible."""
    condition = WEATHER_CODES.get(weather["weather_code"], "Inconnu")
    print("\n" + "=" * 34)
    print(f"  Météo à {name}")
    print("=" * 34)
    print(f"  Conditions  : {condition}")
    print(f"  Température : {weather['temperature_2m']} °C")
    print(f"  Ressenti    : {weather['apparent_temperature']} °C")
    print(f"  Humidité    : {weather['relative_humidity_2m']} %")
    print(f"  Pluie       : {weather['precipitation']} mm")
    print(f"  Vent        : {weather['wind_speed_10m']} km/h")
    print("=" * 34 + "\n")

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