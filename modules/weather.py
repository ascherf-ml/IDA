import requests


def weather():
    api_key = "8ef61edcf1c576d65d836254e11ea420"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    speak=("where do you want to check the weather")
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
        weather=(" Today the temperature is " +
                 str(current_temperature)
                 + "\n but it feels more like "
                 + str(feel_temperature)
                 + "\n . the humidity in percentage is "
                 + str(current_humidiy)
                  + "\n and we have "
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
            weather=(" Today the temperature is " +
                     str(current_temperature)
                     + "\n but it feels more like "
                     + str(feel_temperature)
                     + "its freezing! did you bring a warm jacket? The humidity in percentage is "
                     + str(current_humidiy)
                      + "\n and we have "
                      + str(weather_description))
        elif feel_temperature >=0 and feel_temperature <10:
            weather=(" Today the temperature is " +
                     str(current_temperature)
                     + "\n but it feels more like "
                     + str(feel_temperature)
                     + ". Its cold. the humidity in percentage is "
                     + str(current_humidiy)
                      + "\n and we have "
                      + str(weather_description))
        elif feel_temperature >=10 and feel_temperature <20:
            weather=(" Today the temperature is " +
                     str(current_temperature)
                     + "\n but it feels more like "
                     + str(feel_temperature)
                     + ". Could be warmer, if you ask me. the humidity in percentage is "
                     + str(current_humidiy)
                      + "\n and we have "
                      + str(weather_description))
        elif feel_temperature >=20 and feel_temperature <35:
            weather=(" Today the temperature is " +
                     str(current_temperature)
                     + "\n but it feels more like "
                     + str(feel_temperature)
                     + ". Warm and nice. the humidity in percentage is "
                     + str(current_humidiy)
                      + "\n and we have "
                      + str(weather_description))
        else:
            weather=(" Today the temperature is " +
                     str(current_temperature)
                     + "\n but it feels more like "
                     + str(feel_temperature)
                     + ". Im melting. Can you get me a fan? The humidity in percentage is "
                     + str(current_humidiy)
                      + "\n and we have "
                      + str(weather_description))
        return weather
