# =============================================================================
# Imports
# =============================================================================

import speech_recognition as sr
import pyttsx3
import datetime
import wikipediaapi
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import random
import pandas as pd

# =============================================================================
# Voice output settings
# =============================================================================

engine = pyttsx3.init('sapi5')
wiki_wiki = wikipediaapi.Wikipedia('en')
""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print(rate)  # printing current voice rate
engine.setProperty('rate', 180)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty(
    'volume')  # getting to know current volume level (min=0 and max=1)
print(volume)  # printing current volume level
# setting up volume level  between 0 and 1
engine.setProperty('volume', 0.80)

"""VOICE"""
voices = engine.getProperty('voices')  # getting details of current voice
# changing index, changes voices. 1 for english, 0 for german
engine.setProperty('voice', voices[2].id)


# =============================================================================
# Speech library
# =============================================================================

morning_greet   = ['Good Morning sunshine', 'good morning', 'morning', 'guten tag',
                   'Rise and shine', 'Wakey, wakey, eggs and bakey', 'Good morning, Sleeping Beauty',
                   'I thought you’d never wake up', 'Morning mi amigo!', 'Top o the mornin to ya', 'Rise and shine, its time for wine',
                   'Good morning do you have coffee already', 'how was your night']
midday_greet    = ['Nice to hear from you', 'good to hear you',
                   'nice to hear you', 'its been a while']
afternoon_greet = ['Good Afternoon']
evening_greet   = ['Good Evening']
night_greet     = ['You are still up?']
greet_followers = ['anything else?', 'do you need help with something else?',
                   'what else can i do', 'do you need help with something different',
                   'Im ready if you are']
greet_questions = ['Do you need something from me?', 'Is there something I can help you with?',
                   'What are we doing today?', 'Do you need help?', 'You need something today?',
                   'What are our plans for today', 'Do you have some exiting tasks for me?', 'Let me brighten your day',
                   'Shoot']
greetings       = ['hi', 'hey', 'hello', 'whats up', 'hows it going',
                   'how are you', 'how have you been', 'jello']

# create library and add phrases
phrases = {}
phrases["morning_greet"] = (morning_greet)
phrases["midday_greet"] = (midday_greet)
phrases["afternoon_greet"] = (afternoon_greet)
phrases["evening_greet"] = (evening_greet)
phrases["night_greet"] = (night_greet)
phrases["greet_followers"] = (greet_followers)
phrases["greet_questions"] = (greet_questions)
phrases["greetings"] = (greetings)

# set user name
user = "alex"

# =============================================================================
# IDA Databases
# =============================================================================
main_data_columns = ['text', 'time', 'source', 'command']
main_data = pd.DataFrame(columns=main_data_columns)
todo_data_columns = ['todo', 'date', 'priority']
todo_data = pd.DataFrame(columns=todo_data_columns)
note_data_columns = ['note', 'date']
note_data = pd.DataFrame(columns=note_data_columns)


# =============================================================================
# IDA functions
# =============================================================================


def speak(text):
    engine.say(text)
    engine.runAndWait()

def write(input, source, command, database, database_col):
    data = pd.DataFrame([[input, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), source, command]], columns=database_col)
    database= database.append(data)
    return database

def wishMe():
    global main_data
    global main_data_columns
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 10:
        sentence=(
            f" {random.choice(phrases['greetings'])} {user}. {random.choice(phrases['morning_greet'])}")
        speak(sentence)
        main_data= write(sentence,"IDA","wishme", main_data, main_data_columns)
    elif hour >= 10 and hour < 13:
        sentence=(
            f" {random.choice(phrases['greetings'])} {user}. {random.choice(phrases['midday_greet'])}")
        speak(sentence)
        main_data= write(sentence,"IDA","wishme", main_data, main_data_columns)
    elif hour >= 13 and hour < 17:
        sentence=(
            f" {random.choice(phrases['greetings'])} {user}. {random.choice(phrases['afternoon_greet'])}")
        speak(sentence)
        main_data= write(sentence,"IDA","wishme", main_data, main_data_columns)
    elif hour >= 17 and hour < 20:
        sentence=(
            f" {random.choice(phrases['greetings'])} {user}. {random.choice(phrases['evening_greet'])}")
        speak(sentence)
        main_data= write(sentence,"IDA","wishme", main_data, main_data_columns)
    else:
        sentence=(
            f" {random.choice(phrases['greetings'])} {user}. {random.choice(phrases['night_greet'])}")
        speak(sentence)
        main_data= write(sentence,"IDA","wishme", main_data, main_data_columns)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-EN')

        except Exception as e:
            speak(f"Excuse me {user}, i didn't get that")
            return "None"
        return statement


speak("Ida is starting")
wishMe()


# =============================================================================
# IDA main
# =============================================================================


if __name__ == '__main__':
    global main_data

    wishMe()

    i = 0

    while True:

        if i == 0:
            sentence=random.choice(phrases["greetings"])
            speak(sentence)
            main_data= write(sentence, main_data, main_data_columns)
        else:
            sentence=random.choice(phrases["followers"])
            speak(sentence)
            main_data= write(sentence, main_data, main_data_columns)
            i = i + 1

        statement = takeCommand().lower()
        main_data= write(statement, main_data, main_data_columns)
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('i am shutting down, Good bye')
            print('i am shutting down, Good bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia. What do you want me to find?')
            statement = takeCommand()
            if "no" in statement or "dont" in statement or "stop" in statement:
                speak("Alright")
                print("Wrong command")
            else:
                wikipedia = wiki_wiki.page(statement)
                results = wikipedia.summary[0:500]
                speak(f"According to Wikipedia: {results}")
                print(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("where do you want to check the weather")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"] - 273
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature is " +
                      str(current_temperature)
                      + "\n humidity in percentage is "
                      + str(current_humidiy)
                      + "\n description  "
                      + str(weather_description))
                print(" Temperature in celsius = " +
                      str(current_temperature)
                      + "\n humidity (in percentage) = "
                      + str(current_humidiy)
                      + "\n description = "
                      + str(weather_description))

            else:
                speak(" City Not Found ")

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am IDA version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'openingyour browser ,tell the time,take a photo,search wikipedia,predict weather'
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Mirthula")
            print("I was built by Mirthula")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab(
                "https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, "robo camera", "img.jpg")

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "log off" in statement or "sign out" in statement:
            speak(
                "Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(2)
