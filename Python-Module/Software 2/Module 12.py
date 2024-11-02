import requests

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        joke_data = response.json()
        print(joke_data["value"])
    else:
        print("Failed to retrieve a joke.")

get_chuck_norris_joke()

import requests


def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        description = data["weather"][0]["description"]
        temp_kelvin = data["main"]["temp"]
        temp_celsius = temp_kelvin - 273.15

        print(f"Weather in {city_name}: {description}")
        print(f"Temperature: {temp_celsius:.2f}°C")
    else:
        print("Could not retrieve weather data. Please check the city name and try again.")


if __name__ == "__main__":
    api_key = "434fb6d8c8ccb8ecc9879d7468d3cd50"
    city_name = input("Enter the name of the municipality: ")

    get_weather(city_name, api_key)
