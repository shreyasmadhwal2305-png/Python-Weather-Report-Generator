# WEATHER REPORT GENERATOR


# PART 1 - IMPORTING LIBRARIES

import requests
from datetime import datetime

# requests helps Python communicate with online APIs.
# datetime helps us work with dates and times.

print("================================")
print("       WEATHER REPORT")
print("================================")

print("Weather automation system started!")


# PART 2 - GET CITY INPUT

city = input("\nEnter your city name: ")

# Remove accidental spaces from the beginning and end.
city = city.strip()


# PART 9 - PROFESSIONAL ERROR HANDLING

try:

    # Check whether the user entered a city.
    if not city:
        raise ValueError("City name cannot be empty.")

    print(f"\nFetching weather information for {city}...")


    # PART 3 - FIND CITY COORDINATES

    # Open-Meteo Geocoding API finds a city's coordinates.

    geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"

    parameters = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(
        geocoding_url,
        params=parameters,
        timeout=10
    )

    # Check whether the server returned an HTTP error.
    response.raise_for_status()

    data = response.json()

    if "results" in data and data["results"]:

        location = data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]

        print("\nLocation found!")
        print("City:", location["name"])
        print("Country:", location.get("country", "Unknown"))
        print("Latitude:", latitude)
        print("Longitude:", longitude)

    else:
        raise ValueError("City not found. Please check the spelling.")


    # PART 4 - FETCH CURRENT WEATHER

    # Open-Meteo Weather API provides current weather information.

    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_parameters = {
        "latitude": latitude,
        "longitude": longitude,
        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "apparent_temperature,"
            "is_day,"
            "precipitation,"
            "weather_code,"
            "wind_speed_10m"
        )
    }

    weather_response = requests.get(
        weather_url,
        params=weather_parameters,
        timeout=10
    )

    # Check whether the weather server returned an HTTP error.
    weather_response.raise_for_status()

    weather_data = weather_response.json()

    current_weather = weather_data["current"]

    print("\n========== CURRENT WEATHER ==========")

    print("Temperature:", current_weather["temperature_2m"], "°C")
    print("Feels Like:", current_weather["apparent_temperature"], "°C")
    print("Humidity:", current_weather["relative_humidity_2m"], "%")
    print("Wind Speed:", current_weather["wind_speed_10m"], "km/h")
    print("Precipitation:", current_weather["precipitation"], "mm")
    print("Weather Code:", current_weather["weather_code"])


    # PART 5 - CONVERT WEATHER CODES INTO ENGLISH

    # Weather APIs return numerical weather codes.
    # This dictionary converts them into readable descriptions.

    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snowfall",
        73: "Moderate snowfall",
        75: "Heavy snowfall",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm"
    }

    weather_code = current_weather["weather_code"]

    description = weather_codes.get(
        weather_code,
        "Unknown weather condition"
    )

    print("\nWeather Condition:", description)


    # PART 10 - GET CURRENT DATE AND TIME

    # datetime.now() gets the current local date and time.
    # strftime() converts it into a readable format.

    generated_at = datetime.now().strftime(
        "%d-%m-%Y %I:%M %p"
    )

    print("\nReport Date and Time:", generated_at)


    # PART 6 - GENERATE A WEATHER REPORT

    print("\n" + "=" * 40)
    print("          WEATHER REPORT")
    print("=" * 40)

    print(f"City: {location['name']}")
    print(f"Country: {location.get('country', 'Unknown')}")

    print("-" * 40)

    print(f"Weather: {description}")
    print(f"Temperature: {current_weather['temperature_2m']} °C")
    print(f"Feels Like: {current_weather['apparent_temperature']} °C")
    print(f"Humidity: {current_weather['relative_humidity_2m']}%")
    print(f"Wind Speed: {current_weather['wind_speed_10m']} km/h")
    print(f"Precipitation: {current_weather['precipitation']} mm")

    print(f"Generated At: {generated_at}")

    print("-" * 40)

    print("Report generated successfully!")
    print("=" * 40)


    # PART 7 - SAVE WEATHER REPORT TO A FILE

    # An f-string lets us insert Python variables into the report.

    report = f"""
========================================
          WEATHER REPORT
========================================

City: {location['name']}
Country: {location.get('country', 'Unknown')}

Weather: {description}
Temperature: {current_weather['temperature_2m']} °C
Feels Like: {current_weather['apparent_temperature']} °C
Humidity: {current_weather['relative_humidity_2m']}%
Wind Speed: {current_weather['wind_speed_10m']} km/h
Precipitation: {current_weather['precipitation']} mm

Generated At: {generated_at}

========================================
Report generated successfully!
========================================
"""

    # with open() creates or opens the report file.
    # "w" means write mode.
    # encoding="utf-8" supports special characters.

    with open("weather_report.txt", "w", encoding="utf-8") as file:
        file.write(report)

    print("\nWeather report saved to weather_report.txt!")


    # PART 8 - UNDERSTANDING API ERROR HANDLING

    print("\nAPI ERROR HANDLING")
    print("------------------")
    print("Timeout: The API took too long to respond.")
    print("Connection Error: Unable to connect to the API.")
    print("HTTP Error: The server returned an unsuccessful status.")
    print("Request Error: Another problem occurred during the request.")


# PART 9 - HANDLE DIFFERENT ERRORS

except requests.exceptions.Timeout:

    print("\nError: The API took too long to respond.")


except requests.exceptions.ConnectionError:

    print("\nError: Please check your internet connection.")


except requests.exceptions.HTTPError as error:

    print("\nHTTP Error:", error)


except ValueError as error:

    print("\nError:", error)


except requests.exceptions.RequestException as error:

    print("\nRequest Error:", error)