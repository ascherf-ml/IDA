# =============================================================================
# Imports
# =============================================================================

# standard libraries
import webbrowser
import os
import time
import subprocess
import datetime
import json
import requests
import random

# third party libraries
import speech_recognition as sr
import pyttsx3
import wikipediaapi
import pandas as pd
#from ecapture import ecapture as ec
#import wolframalpha

# local application libraries
import modules.browser
import modules.weather
import modules.speechprocessing



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
engine.setProperty('voice', voices[1].id)


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
                   'how are you', 'how have you been']

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

main_data

# =============================================================================
# IDA functions
# =============================================================================


webbrowser.register('firefox', None, webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))

local_weather("Frankfurt")

# =============================================================================
# IDA main
# =============================================================================


if __name__ == '__main__':
    global main_data
    speak('I am ida. your personal assistant.')
    time.sleep(2)
    wishMe()
    local_weather('Frankfurt')

    i = 0

    while True:

        statement = takeCommand().lower()
        main_data= write(statement, "user","main_talk", main_data, main_data_columns)

        if statement == 0:
            continue

        if "hi" in statement or 'hello' in statement:
            sentence=(f" {random.choice(phrases['greetings'])} {user}")
            speak(sentence)
            main_data= write(statement, "IDA","main_talk", main_data, main_data_columns)

        if "thanks" in statement or 'thank you' in statement:
            sentence=(f"you are welcome")
            speak(sentence)
            main_data= write(statement, "IDA","main_talk", main_data, main_data_columns)


        if "good bye" in statement or "goodbye" in statement or "ok bye" in statement or "shut down" in statement:
            speak('i am shutting down, Good bye')
            main_data= write('shutting down', "IDA","main_talk", main_data, main_data_columns)
            break

        if 'wikipedia' in statement:
            speak('Accessing Wikipedia. What do you want me to find?')
            statement = takeCommand()
            if "no" in statement or "dont" in statement or "stop" in statement:
                speak("Alright")
                print("Wrong command")
            else:
                wikipedia = wiki_wiki.page(statement)
                results = wikipedia.summary[0:500]
                speak(f"According to Wikipedia: {results}")
                print(results)

        elif 'open youtube' in statement or 'youtube' in statement:
            browser('youtube')

        elif 'open google' in statement:
            browser('google')

        elif 'open gmail' in statement:
            browser('gmail')

        elif "weather" in statement:
            weather()


        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am IDA version 1 point O your personal assistant. I am programmed to minor tasks like'
                      'opening your browser ,tell the time,take a photo,search wikipedia,predict weather'
                      'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')

        elif "who made you" in statement or "who created you" in statement:
            speak("I was built by alex")

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
