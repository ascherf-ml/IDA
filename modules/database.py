import pandas as pd
import time

def database_create():
    main_data_columns = ['text', 'time', 'source', 'command']
    main_data = pd.DataFrame(columns=main_data_columns)
    todo_data_columns = ['todo', 'date', 'priority']
    todo_data = pd.DataFrame(columns=todo_data_columns)
    note_data_columns = ['note', 'date']
    note_data = pd.DataFrame(columns=note_data_columns)
    return main_data, main_data_columns

def write(input, source, command, database, database_col):
    data = pd.DataFrame([[input, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), source, command]], columns=database_col)
    database= database.append(data)
    return database


def database_export():
    main_data.to_csv('data/main_data.csv')


def database_import():
    main_data = pd.read_csv('data/main_data.csv',sep=',')
    return main_data
