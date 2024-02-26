from tempfile import NamedTemporaryFile
import shutil
import csv
import datetime

def input_data(): #Ввод данных
    title = input("Введите заголовок заметки: ")
    text = input("Введите заметку: ")

    with open('notes.csv', 'a', encoding='utf-8') as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{title};{text};{timestamp}\n")
        print("Заметка успешно добавлена!")
        
def list_notes(): #Вывод списка заметок
    notes = print_data()
    notes.sort(key=lambda x: x['timestamp'], reverse=True)
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note['title']} - {note['text']} - {note['timestamp']}")

def print_data(): #Вывод данных
    with open('notes.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
    
        j = 0

        notes = []
        for note in data_first:
            note = note.strip()
            title, text, timestamp = note.split(';')
            notes.append({
                'title': title,
                'text': text,
                'timestamp': timestamp
            })

        return notes