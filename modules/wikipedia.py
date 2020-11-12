
import wikipediaapi
from modules.speechprocessing import *

def wikipedia():
    wiki_wiki = wikipediaapi.Wikipedia('de')

    speak('Ich verbinde mich mit Wikipedia. Was soll ich für dich suchen?')
    statement = takeCommand()
    if "nein" in statement or "lass es" in statement or "hör auf" in statement:
        speak("Ok")
    else:
        wikipedia = wiki_wiki.page(statement)
        results = wikipedia.summary[0:500]
        speak(f"Wikipedia zufolge: {results}")
