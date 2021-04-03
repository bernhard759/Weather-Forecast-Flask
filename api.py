# import
from datetime import datetime
import requests
import os


# api key
key = os.environ["Weather_API"]


def getGeo(city):
	"""get geocoordnates"""
	url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={key}"
	response = requests.get(url).json()
	name = response[0]["name"]
	country = response[0]["country"]
	lat = response[0]["lat"]
	lon = response[0]["lon"]
	part = "current,minutely,hourly"
	return lat, lon, part, name, country


def getWeather(lat, lon, part):
	"""get weather forecast"""
	url_forecast = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&units=metric&appid={key}"
	response_forecast = requests.get(url_forecast).json()
	temp_dict = {}
	weather_dict = {}
	for day in response_forecast["daily"]:
		temp_dict[datetime.strptime(str(datetime.fromtimestamp(day["dt"])), "%Y-%m-%d %X").strftime("%A")] = day["temp"]["day"]
		weather_dict[datetime.strptime(str(datetime.fromtimestamp(day["dt"])), "%Y-%m-%d %X").strftime("%A")] = day["weather"][0]["description"], day["weather"][0]["icon"]
	print(weather_dict)
	return temp_dict, weather_dict


if __name__ == "__main__":
	lat, lon, part, name, country = getGeo("Weiden")
	print(getWeather(lat, lon, part))