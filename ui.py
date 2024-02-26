from logger import input_data, list_notes, delete_data, change_data

def interface():
    print("Добрый день! Вас приветствует справочник! Выберите необходимое действие:\n 1 – Создать заметку \n 2 - Редактировать заметку \n 3 – Удалить заметку \n 4 – Посмотреть список заметок \n 5 - Выход")
    command = int(input('Введите число: '))

    while command < 1 or command >= 6:
        print("Неправильный ввод")
        command = int(input('Введите число: '))
    if command == 1:
        input_data()
    elif command == 2:
        change_data()
    elif command == 3:
        delete_data() 
    elif command == 4:
        list_notes()
    elif command == 5:
        print('До свидания!')