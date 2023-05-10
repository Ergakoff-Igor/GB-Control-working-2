class Note:

    def __init__(self, id, date, heading, body):
        self._id = id                # ID
        self._date = date            # Дата
        self._heading = heading      # Заголовок
        self._body = body            # Тело записи

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return str(self._id)
    
    def set_date(self, date):
        self._date = date

    def get_date(self):
        return str(self._date)

    def set_heading(self, heading):
        self._heading = heading

    def get_heading(self):
        return str(self._heading)       
    
    def set_body(self, body):
        self._body = body

    def get_body(self):
        return str(self._body)
    
    def __str__(self):
        return f"ID: {self._id}   Дата: {self._date}   Заголовок: {self._heading}"

    def display_info(self):
        print(f"ID: {self._id}")
        print(f"Дата создания/изменения заметки: {self._date}")
        print(f"Заголовок: {self._heading}")
        print(f"Тело заметки:\n{self._body}")