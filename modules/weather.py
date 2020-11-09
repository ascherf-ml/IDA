import requests

from modules.speechprocessing import *


def weather():
    api_key = "8ef61edcf1c576d65d836254e11ea420"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    speak("wo soll ich nach dem wetter schauen?")
    city_name = takeCommand()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = round(float(y["temp"] - 273), 2)
        feel_temperature = round(float(y["feels_like"] - 273), 1)
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        weather=(" Heute ist es  " +
                 str(current_temperature)
                 + " grad. Aber es fühlt sich eher nach "
                 + str(feel_temperature)
                 + " an . Luftfeuchtigkeit beträgt "
                 + str(current_humidiy)
                  + " Prozent und wir haben "
                  + str(weather_description))

    else:
        weather=(" City Not Found ")
    return weather

def local_weather(city):
    api_key = "8ef61edcf1c576d65d836254e11ea420"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = round(float(y["temp"] - 273), 1)
        feel_temperature = round(float(y["feels_like"] - 273), 1)
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        if feel_temperature <0:
            weather=(" Heute ist es  " +
                     str(current_temperature)
                     + "grad. Aber es fühlt sich eher nach "
                     + str(feel_temperature)
                     + "an. Es ist super kalt! Ich hoffe du hast eine warme Jacke eingepackt. Die Luftfeuchtigkeit beträgt "
                     + str(current_humidiy)
                      + " Prozent und wir haben "
                      + str(weather_description))
        elif feel_temperature >=0 and feel_temperature <10:
            weather=(" Heute ist es  " +
                     str(current_temperature)
                     + "grad. Aber es fühlt sich eher nach "
                     + str(feel_temperature)
                     + "an. Du brauchst heute auf jeden Fall eine warme Jacke. Die Luftfeuchtigkeit beträgt "
                     + str(current_humidiy)
                      + " Prozent und wir haben "
                      + str(weather_description))
        elif feel_temperature >=10 and feel_temperature <20:
            weather=(" Heute ist es  " +
                     str(current_temperature)
                     + "grad. Aber es fühlt sich eher nach "
                     + str(feel_temperature)
                     + "an. Es könnte wärmer sein, wenn du mich fragst. Die Luftfeuchtigkeit beträgt "
                     + str(current_humidiy)
                      + " Prozent und wir haben "
                      + str(weather_description))
        elif feel_temperature >=20 and feel_temperature <35:
            weather=(" Heute ist es  " +
                     str(current_temperature)
                     + "grad. Aber es fühlt sich eher nach "
                     + str(feel_temperature)
                     + "an. Schön warm. Die Luftfeuchtigkeit beträgt "
                     + str(current_humidiy)
                      + " Prozent und wir haben "
                      + str(weather_description))
        else:
            weather=(" Heute ist es  " +
                     str(current_temperature)
                     + "grad. Aber es fühlt sich eher nach "
                     + str(feel_temperature)
                     + "an. Mein Motherbord schwitzt. Die Luftfeuchtigkeit beträgt "
                     + str(current_humidiy)
                      + " Prozent und wir haben "
                      + str(weather_description))
        return weather
