import telebot
from api import bot
from get_data import get_temp_and_date 
from get_data import get_temp_and_date_night
from log import log


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Напиши город на русском языке и я покажу какая будет погода ")

    # Обрабатываем входящие текстовые сообщения
@bot.message_handler(content_types=['text'])
def get_weather(message):
    city_name = message.text.strip().lower() #переменная для функции
    if get_temp_and_date(city_name):
        if get_temp_and_date_night(city_name):
            weather_message = (
                f"Данные по  городу  {city_name.title()}: \nТемпература {(get_temp_and_date(city_name))['temperature']}: {(get_temp_and_date(city_name))['status']}\n" 
                f"Влажность: {(get_temp_and_date(city_name))['humidity']}\n" 
                f"Давление: {(get_temp_and_date(city_name))['pressure']} \n" 
                f"Скорость ветра: {(get_temp_and_date(city_name))['wind_speed']}\n" 
                f"Дата и время: {(get_temp_and_date(city_name))['date']}\n"
                f"Температура в полночь: {(get_temp_and_date_night(city_name))['cur_tem']}"
            )
    else:
        weather_message = f"Извините, не удалось получить данные о погоде в городе {city_name.title()}. Пожалуйста, проверьте правильность названия города и попробуйте еще раз."
    bot.send_message(message.chat.id, weather_message)
    log(message) # log

bot.polling(none_stop=True)