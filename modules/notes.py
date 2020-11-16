from modules.database import *
from modules.config import *
from modules.speechprocessing import *

note_data= note_database_import()



def notebook():
    while True:
        speak('Dein Notizbuch ist offen, was soll ich tun?')
        statement = takeCommand()

        if "neue notiz" in statement or 'notiz anlegen' in statement or 'notizen anlegen' in statement or 'neue notizen' in statement:
            speak('Was soll ich notieren?')
            statement = takeCommand()
            note_data= write(statement, "IDA","main_talk", main_data, main_data_columns)
            while True:
                speak('Willst du noch noch eine Notiz anlegen?')
                if "ja" in statement or "gerne" in statement:
                    speak('Was soll ich notieren?')
                    statement = takeCommand()
                    note_data= write(statement, "IDA","main_talk", main_data, main_data_columns)

                if "nein" in statement or "das reicht" in statement:
                    speak('Alles klar')
                    break

        if "notizen anhören" in statement or 'anhören' in statement or 'durchgehen' in statement:



        if "das reicht" in statement or 'reicht' in statement or 'mach es zu' in statement or 'zurück' in statement:
            speak('Alles klar, ich mach es wieder zu.')
            break









note_data= write(statement, "user","main_talk", note_data, note_data_columns)
