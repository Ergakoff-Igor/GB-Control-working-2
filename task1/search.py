# Метод поиска по ID
def search_by_id(answer, array):
    for note in array:
        if note.get_id() == answer:
            note.display_info()
            return True
    return False

# Метод поиска по заголовку
def search_by_heading(answer, array):
    for note in array:
        if note.get_heading() == answer:
            note.display_info()
            return True
    return False

# Метод поиска по дате
def search_by_data(answer, array):
            count = 0
            for note in array:
                if note.get_date() == answer:
                    print(note)
                    count += 1
            if count == 0:
                return False
            else: 
                return True