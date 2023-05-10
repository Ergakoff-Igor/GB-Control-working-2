from note import Note
from datetime import datetime as dt
import importer as imp
import exporter as exp
import search

notebook = []

def add_new_note (file, heading, body):
    notebook = load(file)
    id = "{}".format(len(notebook) + 1)
    date = dt.now().strftime('%Y-%m-%d') 
    note = Note(id, date, heading, body)      
    notebook.append(note)
    try:
        save(file,notebook)
        print('Заметка успешно сохранена')
    except:
        print('Ошибка записи')


def save (file,notebook):
    exp.save_data_to_file(file,notebook)


def load(file):
    return imp.read_data_from_file(file)


