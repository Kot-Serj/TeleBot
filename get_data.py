import requests
from api import api

#функция +- 3 часа 
def get_temp_and_date(city_name : str ):
    try:
        r = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&cnt=1&lang=ru&units=metric&appid={api}')
        resp = r.json()
        for weather in resp['list']:
            data_des = weather['weather'][0]['description']
            cur_temp = weather["main"]["temp"]
            humidity = weather["main"]["humidity"]
            pressure = weather["main"]["pressure"]
            wind = weather["wind"]["speed"]
            times = weather["dt_txt"]
            return {
                'status': data_des,
                'temperature': cur_temp,
                'humidity': humidity,
                'pressure': pressure,
                'wind_speed': wind,
                'date': times
            }
    except:
        return None

def get_temp_and_date_night(city_name : str ):
    try:
        q = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&cnt=10&lang=ru&units=metric&appid={api}')
        data = q.json()
        for forecast in data["list"]:
            date, time = forecast["dt_txt"].split(" ")
            if time == "00:00:00":
                night=(forecast["dt_txt"])
                cur_temper = forecast["main"]["temp"]
                return {
                    'night_time': night,
                    'cur_tem': cur_temper
                }
    except:
        return None


    