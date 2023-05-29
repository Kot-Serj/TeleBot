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


    