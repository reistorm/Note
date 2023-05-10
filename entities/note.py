import datetime

class Note:
    __note_id: int
    __title: str = ""
    __date_of_change: str = ""
    __text: str = ""

    def __init__(self, title, text, note_id: int = 0, date_of_change: str = ''):
        self.__note_id = note_id
        self.__title = title
        self.set_date_of_change(date_of_change)
        self.__text = text

    def get_id(self) -> int:
        return self.__note_id

    def get_title(self) -> str:
        return self.__title

    def set_title(self, title: str):
        self.__title = title
        self.set_date_of_change()

    def set_date_of_change(self, date_of_change: str = ''):
        if date_of_change == '':
            self.__date_of_change = self.__get_data()
        else:
            self.__date_of_change = date_of_change

    def get_date_of_change(self) -> str:
        return self.__date_of_change

    def get_text(self) -> str:
        return self.__text

    def set_text(self, text: str):
        self.__text = text
        self.set_date_of_change()

    def __get_data(self):
        return datetime.datetime.today().strftime("%d.%m.%Y-%H:%M:%S")

    def to_string(self) -> str:
        if self.__note_id !=0:
            return f"id:{self.__note_id}\tdate_of_change:{self.__date_of_change}\ntitle:{self.__title}\ntext:{self.__text}\n"
        else:
            return f"title:{self.__title}\n"