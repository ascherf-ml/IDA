import speech_recognition as sr
import pyttsx3
import datetime
import random


def speak(text):
    speech_engine()
    engine.say(text)
    engine.runAndWait()

def write(input, source, command, database, database_col):
    data = pd.DataFrame([[input, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), source, command]], columns=database_col)
    database= database.append(data)
    return database

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-EN')

        except Exception as e:
            #speak(f"Excuse me {user}, i didn't get that")
            return "None"
        return statement

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

def speech_engine():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    engine.setProperty('rate', 180)     # setting up new voice rate


    """VOLUME"""
    volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    # setting up volume level  between 0 and 1
    engine.setProperty('volume', 0.80)

    """VOICE"""
    voices = engine.getProperty('voices')  # getting details of current voice
    # changing index, changes voices. 1 for english, 0 for german
    engine.setProperty('voice', voices[0].id)

    return engine
