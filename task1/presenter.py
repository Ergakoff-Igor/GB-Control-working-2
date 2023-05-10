import os
import time
import console_viewer as cv
import model as mod

# Метод очистки консоли
def clear_screen():
    os.system('cls')

# Метод поиска заметки
def search_date(file, array):
    while True:
        answer = cv.notebook_actions()
        match answer:
            case "1":
                # Показать запись по номеру
                clear_screen()
                num = cv.get_id()
                if mod.search.search_by_id(num, array): 
                    print('Запись под номером {}:'.format(num))
                    cv.note_menu(file, num, array)
                else:
                    print ("Записи под номером {} не обнаружено".format(num))
                    time.sleep(3)
                    print_all_date(file)
            case "2":
                # Показать запись по заголовку
                clear_screen()
                answer = cv.get_heading()
                if mod.search.search_by_heading(answer, array): 
                    print('Запись c заголовком {}:'.format(answer))
                    pass
                else:
                    print ("Записи c заголовком {} не обнаружено".format(answer))
                    time.sleep(3)
                    print_all_date(file)                
            case "3":
                # Показать записи по дате 
                clear_screen()
                data = cv.get_date()
                if mod.search.search_by_data(data, array): 
                    print('Все записи от {}:'.format(data))
                    pass       
                else:
                    print('Pаписи от {} не обнаружено'.format(data))
                    time.sleep(3)
                    print_all_date(file)
            case "0":
                #выход
                cv.Menu.menu()                 
            case _:
                clear_screen()
                print("неверный ввод")
                time.sleep(1) 

# Метод вывода всех заметок
def print_all_date(file):
    clear_screen()
    array = mod.load(file)
    for note in array:
        print(note)
    search_date(file, array)      

# Метод добавления новой заметки
def add_note(file):
    clear_screen()
    print('Добавление заметки:')
    head = cv.get_heading()
    body = cv.get_body()
    mod.add_new_note(file, head, body)
    
    
# Удаление заметки
def dell_date(file, num, array):
    new_array = []
    count = 0
    for line in array:
        if line.get_id() != num:
            count+=1
            line.set_id(count)
            new_array.append(line)
    mod.save(file, new_array)

# Метод изменения заметок
def change_date(file, num, array, id):
    new_array = []
    for line in array:
        if line.get_id() == id and num == "1":
            print("Старый заголовок: {}".format(line.get_heading()))
            new_heading = cv.get_heading()
            line.set_heading(new_heading)
        elif line.get_id() == id and num == "2":
            print("Старое тело записи: \n{}".format(line.get_body()))
            new_body = cv.get_body()
            line.set_body(new_body)
        new_array.append(line)
    mod.save(file, new_array)    