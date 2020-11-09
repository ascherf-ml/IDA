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
    speak('Hallo, ich bin Ida, dein persönlicher Assistent')
    time.sleep(2)
    wishMe()
    local_weather('Frankfurt')

    i = 0

    while True:

        statement = takeCommand().lower()
        main_data= write(statement, "user","main_talk", main_data, main_data_columns)

        if statement == 0:
            continue

        if "hi" in statement or 'hallo' in statement or 'grüß dich' in statement:
            sentence=(f" {random.choice(phrases['greetings'])} {user}")
            speak(sentence)
            main_data= write(statement, "IDA","main_talk", main_data, main_data_columns)

        if "danke" in statement:
            sentence=(f"Gerne")
            speak(sentence)
            main_data= write(statement, "IDA","main_talk", main_data, main_data_columns)


        if "tschüss" in statement or "schalte dich ab" in statement or "das reicht für heute" in statement or "schalte dich aus" in statement:
            speak(f'Ich schalte mich ab. bis zum nächsten mal {user}')
            main_data= write('shutting down', "IDA","main_talk", main_data, main_data_columns)
            break

        if 'wikipedia' in statement:
            speak('Ich verbinde mich mit Wikipedia. Was soll ich für dich suchen?')
            statement = takeCommand()
            if "nein" in statement or "lass es" in statement or "hör auf" in statement:
                speak("Ok")
                print("Wrong command")
            else:
                wikipedia = wiki_wiki.page(statement)
                results = wikipedia.summary[0:500]
                speak(f"Wikipedia zufolge: {results}")
                print(results)

        elif 'öffne youtube' in statement or 'youtube' in statement:
            browser('youtube')
            speak(f"Youtube ist jetzt offen")

        elif 'öffne google' in statement:
            browser('google')
            speak(f"Google ist jetzt offen")

        elif 'öffne gmail' in statement or 'öffne google mail' in statement:
            browser('gmail')
            speak(f"Gmail ist jetzt offen")

        elif "wetter" in statement:
            weather()

        elif 'suche nach' in statement:
            statement = statement.replace("suche", "")
            statement = statement.replace("nach", "")
            browser(statement)

        elif "öffne stackoverflow" in statement:
            browser('stackoverflow')

        elif 'nachrichten' in statement:
            browser('news.google')


        elif 'zeit' in statement or 'uhrzeit' in statement or 'uhr' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Es ist {strTime}")

        elif 'wer bist du' in statement:
            speak('Ich bin Ida. Version 0 Punkt eins. Dein persönlicher assistent')

        elif "dich gemacht" in statement or "erschaffen" in statement:
            speak("Ich wurde von Alex gemacht")


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
