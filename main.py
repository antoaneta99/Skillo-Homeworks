# Homework 12
# Problem 0:
# Choose a public API of your choice (e.g., weather, news, or any other available API).
# Write a Python program that makes a GET request to the chosen API.
# Retrieve data from the API and display specific information from the response.
# Ensure error handling for cases where the request may fail.
import requests

api_key = '5c977b3afcf849e9157918c2ad5b815a'
city = 'Sofia'
def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        temperature_celsius = weather_data['main']['temp'] - 273.15

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature_celsius:.0f} Celsius")
        print(f"Description: {weather_data['weather'][0]['description']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


get_weather(api_key, city)

# Problem 1:
# Find a public API that provides data in JSON format.
# Create a Python program to fetch data from this API and parse it as JSON.
# Implement a feature that allows users to interact with the data (e.g., search, filter, or manipulate the JSON data).
# Public APIs: https://documenter.getpostman.com/view/8854915/Szf7znEe
def fetch_and_interact(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()

        print("Weather data:")
        for key, value in weather_data.items():
            print(f"{key}: {value}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


api_key = '5c977b3afcf849e9157918c2ad5b815a'
city = 'Sofia'

fetch_and_interact(api_key, city)