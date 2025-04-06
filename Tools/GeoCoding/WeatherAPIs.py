from Tools.GeoCoding.state_codes import *
from API_keys.OpenWeather import *
from Tools.pattern_match import *
import requests as rq
import json

api_key = OpenWeatherAPI_key()

def geocoding(city_name, state_code):
    lat, lon = None, None
    geo_response = rq.get(f"https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},US&appid={api_key}")
    if geo_response.status_code == 200:
        locinfojson = geo_response.content.decode('utf-8')
        locinfodict = json.loads(locinfojson)
        # print(locinfodict[0])
        lat = locinfodict[0]['lat']
        lon = locinfodict[0]['lon']
    else:
        print("there was an error: ", geo_response.status_code)
    return lat, lon

def forecasting(latt, long):
    for_response = rq.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latt}&lon={long}&appid={api_key}&units=imperial")
    if for_response.status_code == 200:
        forecastjson = for_response.content.decode('utf-8')
        forecastdict = json.loads(forecastjson)
        # print(forecastdict)
        temp = forecastdict['main']['temp']
        # print("temperature: ", temp)

        feelslike = forecastdict['main']['feels_like']
        # print("feels like: ", feelslike)

        tmax = forecastdict['main']['temp_max']
        # print("max temp: ", max)

        tmin = forecastdict['main']['temp_min']
        # print("min temp: ", min)

        descr = forecastdict['weather'][0]['description']
        # print("description :", descr)
        forecast = [temp, feelslike, tmax, tmin, descr]
        return forecast
    else:
        print("there was an error: ", for_response.status_code)
        return None, None, None, None, None

def weather(text):
    location_error = False
    # access weather API
    raw_location = get_pattern_match('in ([a-zA-Z]*, [a-zA-Z]*)|forecast for ([a-zA-Z]* [a-zA-Z]*)|in ([a-zA-Z]* [a-zA-Z]*)', text)
    if raw_location is None:
        location_error = True
        return None, None, location_error
    try:
        city = get_pattern_match('([a-z]*),|([a-z]*) ', raw_location[0])
        raw_state = get_pattern_match('.* ([A-z]*)', raw_location[0])
        state_code = get_state_code(raw_state.lower())
        location = f"{city[0]} {state_code}"
        lat, lon = geocoding(city[0], state_code)
        forecast = forecasting(lat, lon)
    except Exception as e:
        city = get_pattern_match('([a-z]*),|([a-z]*) ', raw_location[2])
        raw_state = get_pattern_match('.* ([A-z]*)', raw_location[2])
        state_code = get_state_code(raw_state.lower())
        location = f"{city[1]} {state_code}"
        lat, lon = geocoding(city[1], state_code)
        forecast = forecasting(lat, lon)

    return forecast, location, location_error  # forecast

if __name__ == "__main__":
    forecast, location, location_error = weather("weather in lubbock texas")
    print(forecast, location, location_error)