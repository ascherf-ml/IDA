import pandas as pd
import time

from modules.database import *
from modules.config import *
from modules.speechprocessing import *

note_data_columns = ['note', 'date']
note_data = pd.DataFrame(columns=note_data_columns)

def notebook():
    while True:

        speak('Dein Notizbuch ist offen, was soll ich tun?')
        statement = takeCommand()

        if "neue notiz" in statement or 'anlegen' in statement or 'erstellen' in statement or 'neue notizen' in statement:
            speak('Was soll ich notieren?')
            statement = takeCommand()
            note_data= write_note(statement)
            while True:
                speak('Willst du noch noch eine Notiz anlegen?')
                if "ja" in statement or "gerne" in statement:
                    speak('Was soll ich notieren?')
                    statement = takeCommand()
                    note_data= write_note(statement)

                if "nein" in statement or "das reicht" in statement:
                    speak('Alles klar')
                    break

        #if "notizen anhören" in statement or 'anhören' in statement or 'durchgehen' in statement:

        if "das reicht" in statement or 'reicht' in statement or 'mach es zu' in statement or 'zurück' in statement:
            speak('Alles klar, ich mach es wieder zu.')
            break



notebook()





note_data= write(statement, "user","main_talk", note_data, note_data_columns)
