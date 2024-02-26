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

def change_data(): #Редактирование данных
    notes = print_data()
    list_notes()
    note_index = int(input("Введите номер заметки, которую необходимо отредактировать: ")) - 1
    note = notes[note_index]
    note['title'] = input("Введите новый заголовок заметки: ")
    note['text'] = input("Введите новую заметку: ")
    note['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open('notes.csv', 'w', encoding='utf-8') as f:
        text = ''.join(f'{note['title']};{note['text']};{note['timestamp']}\n' for note in notes)
        f.write(text)
        print("Заметка успешно отредактирована!")

def delete_data(): #Удаление данных
    notes = print_data()
    list_notes()
    note_index = int(input("Введите номер заметки, которую необходимо удалить: ")) - 1
    del notes[note_index]

    with open('notes.csv', 'w', encoding='utf-8') as f:
        text = ''.join(f'{note['title']};{note['text']};{note['timestamp']}\n' for note in notes)
        f.write(text)
        print("Заметка успешно удалена!")
        
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