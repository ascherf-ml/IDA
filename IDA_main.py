# =============================================================================
# Imports
# =============================================================================

# standard libraries

import os
import time
import subprocess
import datetime
import pyttsx3

import json
import random

# third party libraries

import wikipediaapi
import pandas as pd
#from ecapture import ecapture as ec
#import wolframalpha

# local application libraries
from modules.browser import *
from modules.weather import *
from modules.speechprocessing import *



# =============================================================================
# Voice output settings
# =============================================================================

wiki_wiki = wikipediaapi.Wikipedia('en')

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
speak('hallo')

webbrowser.register('firefox', None, webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))

speak(local_weather("Frankfurt"))

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

        elif 'search' in statement:
            statement = statement.replace("search", "")
            statement = statement.replace("for", "")
            browser(statement)

        elif "open stackoverflow" in statement:
            browser('stackoverflow')

        elif 'show news' in statement:
            browser('news.google')


        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am IDA version 0 point 1. your personal assistant')

        elif "who made you" in statement or "who created you" in statement:
            speak("I was built by alex")


        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, "robo camera", "img.jpg")


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
