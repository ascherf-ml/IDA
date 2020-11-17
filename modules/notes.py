# =============================================================================
# Imports
# =============================================================================
# standard libraries
import pandas as pd
import time
import numpy as np

# local application libraries
from modules.config import *
from modules.speechprocessing import *

# =============================================================================
# setting up database (ONLY ONCE)
# =============================================================================

note_data_columns = ['note', 'date', 'short_date']
note_data = pd.DataFrame(columns=note_data_columns)
note_data.to_csv('data/note_data.csv', index=False)

# =============================================================================
# notebook functions
# =============================================================================
def write_note(input):
    note_data = pd.read_csv('data/note_data.csv',sep=',')
    note_data_columns = ['note', 'date', 'short_date']
    data = pd.DataFrame([[input, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), time.strftime("%Y-%m-%d %H:%M", time.localtime())]], columns=note_data_columns)
    new_note= note_data.append(data)
    new_note.to_csv('data/note_data.csv',index=False)
    return new_note

# =============================================================================
# notebook main
# =============================================================================
def notebook():
    note_data = pd.read_csv('data/note_data.csv',sep=',')
    speak('Dein Notizbuch ist offen, was soll ich tun?')

    while True:
        statement = takeCommand()
        if "neue notiz" in statement or 'anlegen' in statement or 'erstellen' in statement or 'neue notizen' in statement:
            speak('Was soll ich notieren?')
            statement = takeCommand()
            write_note(statement)
            while True:
                speak('Willst du noch eine Notiz anlegen?')
                statement = takeCommand()

                if "ja" in statement or "gerne" in statement or 'noch eine' in statement:
                    speak('Was soll ich notieren?')
                    statement = takeCommand()
                    write_note(statement)

                if "nein" in statement or "das reicht" in statement:
                    speak('Alles klar')
                    break

        if "notizen anhören" in statement or 'anhören' in statement or 'durchgehen' in statement or 'durch gehen' in statement:
            for index, row in note_data.iterrows():
                speak(f" Am {row['short_date']} hast du dir notiert: {row['note']}")

        timeout = time.time() + 60
        if time.time() > timeout:
            note_data[['note','date']].reindex().to_csv('data/note_data.csv')
            return note_data
            break

        if 'notizbuch zumachen' in statement or 'mach es zu' in statement or 'zumachen' in statement or 'zurück' in statement or 'buch zumachen' in statement or 'schließen' in statement:
            speak('Ich mach es wieder zu.')
            break
