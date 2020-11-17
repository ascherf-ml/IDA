import pandas as pd
import time

def main_database_columns_create():
    main_data_columns = ['text', 'time', 'source', 'command']

def main_database_create():
    main_data = pd.DataFrame(columns=main_data_columns)


def todo_database_create():
    todo_data_columns = ['todo', 'date', 'priority']
    todo_data = pd.DataFrame(columns=todo_data_columns)

def note_database_create():
    note_data_columns = ['note', 'date']
    note_data = pd.DataFrame(columns=note_data_columns)
    return note_data, note_data_columns


def write(input, source, command, database, database_col):
    data = pd.DataFrame([[input, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), source, command]], columns=database_col)
    database= database.append(data)
    return database




def database_export():
    main_data.to_csv('data/main_data.csv')
    note_data.to_csv('data/note_data.csv')


def database_import():
    main_data = pd.read_csv('data/main_data.csv',sep=',')
    return main_data

def note_database_import():
    note_data = pd.read_csv('data/note_data.csv',sep=',')
    return note_data
