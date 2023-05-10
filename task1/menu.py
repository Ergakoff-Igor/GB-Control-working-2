import time
import presenter as pres

DATE = 'date.csv'

def menu():
    while True:
        menu = '''Главное меню:\n
    1 - Вывод всех заметок
    2 - Добавление заметки
    0 - Выход\n'''

        pres.clear_screen()
        print(menu)
        answer = input('Введите номер действия: ')
        match answer:
            case "1":
                # Вывод всех заметок
                pres.print_all_date(DATE)
            case "2":
                # Добавление заметки
                pres.add_note(DATE)
            case "0":
                #выход
                pres.clear_screen()
                print("До свидания !!!")
                time.sleep(1) 
                exit(0)                 
            case _:
                pres.clear_screen()
                print("неверный ввод")
                time.sleep(1) 



