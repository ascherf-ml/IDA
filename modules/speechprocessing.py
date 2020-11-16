import speech_recognition as sr
import datetime
import random
import pandas as pd
import time

import boto3
import io
import pygame

from modules.database import *
from modules.config import *

pygame.init()
pygame.mixer.init()

main_data= main_database_create()


def speak_ssml(message):
    polly = boto3.client('polly')
    response = polly.synthesize_speech(OutputFormat='mp3', VoiceId='Vicki',TextType='ssml',
                 Text=message)
    audio = io.BytesIO(response['AudioStream'].read())
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def speak(message):
    polly = boto3.client('polly')
    response = polly.synthesize_speech(OutputFormat='mp3', VoiceId='Vicki',
                 Text=message)
    audio = io.BytesIO(response['AudioStream'].read())
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='de-DE')

        except Exception as e:
            speak(f"Das habe ich nicht verstanden")
            return "None"
        return statement

def background_listening():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='de-DE')

        except Exception as e:
            return "None"
        return statement

def wishMe():
    global main_data
    global main_data_columns
    hour = datetime.datetime.now().hour
    engine = speech_engine()
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


morning_greet   = ['Guten Morgen', 'guten morgen sonnenschein', 'morgen!', 'einen guten morgen',
                   'Gut geschlafen?', 'wie war deine nacht?',
                   'Guten morgen, hattest du schon einen Kaffee']
midday_greet    = ['Schön dich zu hören', 'schön von dir zu hören',
                   'grüß dich', 'hallo']
afternoon_greet = ['Schönen nachmittag']
evening_greet   = ['Guten abend']
night_greet     = ['ganz schön spät']
greet_followers = ['sonst noch etwas?', 'kann ich noch etwas für dich tun?']
greet_questions = ['kann ich etwas für dich tun?', 'was kann ich für dich tun?',
                   'was machen wir heute?', 'brauchst du hilfe bei etwas?', 'brauchst du etwas?',
                   'was sind die pläne für heute?', 'irgendetwas aufregendes heute für mich zu tun','was gibts']
greetings       = ['hi', 'hey', 'hallo', 'was gibts', 'wie gehts',
                   'wie gehts dir']

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
