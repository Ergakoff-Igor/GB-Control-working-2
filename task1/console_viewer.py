import time
import presenter as pres
import menu as Menu


def get_heading():
    return input('Введите заголовок >>> ')

def get_body():
    return input('Введите текст заметки >>> ')

def get_id():
    return input('Введите номер заметки >>> ')

def get_date():
    day = input('день >>> ')
    mounth = input('месяц >>> ')
    year = input('год >>> ')
    data = "{}-{}-{}".format(year, mounth, day)
    print(data)
    return data


def notebook_actions():
    # while True:
    menu = '''Меню списка заметок:\n
1 - Показать запись по номеру
2 - Показать запись по заголовку
3 - Показать записи по дате 
0 - Выход\n'''
    
    print(menu)
    return input('Введите номер действия: ')

        # match answer:
        #     case "1":
        #         # Показать запись по номеру
        #         pres.clear_screen()
        #         num = get_id()
        #         pres.search_date(file, num, answer, array)
        #     case "3":
        #         # Показать записи по дате 
        #         pres.clear_screen()
        #         data = get_date()
        #         if pres.search_date(answer, data, array): 
        #             print('Все записи от {}:'.format(data))
        #             pres.search_date(answer, data, array)       
        #         else:
        #             print('Pаписи от {} не обнаружено'.format(data))
        #             time.sleep(3)
        #             pres.print_all_date(file)
        #     case "0":
        #         #выход
        #         Menu.menu()                 
        #     case _:
        #         pres.clear_screen()
        #         print("неверный ввод")
        #         time.sleep(1) 

def note_menu(file, num, array):
    while True:
        menu = '''Действия с заметкой:\n
    1 - Изменить заголовок
    2 - Изменить тело заметки 
    3 - Удалить заметку
    0 - Выход\n'''
        
        print(menu)
        answer = input('Введите номер действия: ')
        match answer:
            case "1":
                # Изменить заголовок
                pres.clear_screen()
                print('Изменение заголовка записи под номером {}:'.format(num))
                pres.change_date(file, answer, array, num) 
                pres.print_all_date(file)  
            case "2":
                # Изменить тело заметки 
                pres.clear_screen()
                print('Изменение тела записи под номером {}:'.format(num))
                pres.change_date(file, answer, array, num) 
                pres.print_all_date(file)
            case "3":
                # Удаление заметки
                pres.clear_screen()
                if del_menu():
                    pres.dell_date(file, num, array)   
                else: 
                    pres.print_all_date(file)              
            case "0":
                #выход
                pres.print_all_date(file)                 
            case _:
                pres.clear_screen()
                print("неверный ввод")
                time.sleep(1) 

def del_menu():
    while True:
        menu = '''Вы действительно хотите удалить эту запись?:\n
    1 - Да
    2 - Нет\n'''
        
        print(menu)
        answer = input('Введите номер действия: ')
        match answer:
            case "1":
                return True   
            case "2":
                return False              
            case _:
                pres.clear_screen()
                print("неверный ввод")
                time.sleep(1) 
