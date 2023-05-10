import json
import os.path
from entities import Note


class DbJsonRequests:
    __db_path: str

    def __init__(self, db_path):
        self.__db_path = db_path

    def create_table(self):
        notes: dict = {'max_id': 0, 'notes':[]}
        self.__set_table(notes=notes)

    def check_exist_table(self) -> bool:
        return os.path.exists(self.__db_path)


    def select_all_notes(self) -> list:
        data: dict = self.__get_table()
        notes_data: list = data.get("notes")
        notes_list: list = []
        if notes_data != []:
            for note in notes_data:
                notes_list.append(Note(note_id = note.get("note_id"),
                                     title=note.get("title"),
                                       text=note.get("text"),
                                       date_of_change=note.get("date_of_change")))
        return notes_list

    def select_note_by_id(self, id: int) -> Note:
        data: dict = self.__get_table()
        notes_data: list = data.get("notes")
        if notes_data != []:
            for note in notes_data:
                if note.get("note_id") == id:
                    return Note(note_id = note.get("note_id"),
                                     title=note.get("title"),
                                       text=note.get("text"),
                                       date_of_change=note.get("date_of_change"))
        return Note(title="Запись отсутствует", text="")


    def select_notes_by_title(self, title: str) -> list:
        data: dict = self.__get_table()
        notes_data: list = data.get("notes")
        notes_list: list = []
        if notes_data != []:
            for note in notes_data:
                if title in note.get("title").lower():
                    notes_list.append(Note(note_id=note.get("note_id"),
                                       title=note.get("title"),
                                       text=note.get("text"),
                                       date_of_change=note.get("date_of_change")))
        return notes_list

    def select_notes_by_date(self, date_of_change: str) -> list:
        data: dict = self.__get_table()
        notes_data: list = data.get("notes")
        notes_list: list = []
        if notes_data != []:
            for note in notes_data:
                if date_of_change in note.get("date_of_change"):
                    notes_list.append(Note(note_id=note.get("note_id"),
                                       title=note.get("title"),
                                       text=note.get("text"),
                                       date_of_change=note.get("date_of_change")))
        return notes_list

    def update_note(self, note: Note):
        data: dict = self.__get_table()
        notes_data: list = data.get("notes")
        for n in notes_data:
            if n.get("note_id") == note.get_id():
                n["title"] = note.get_title()
                n["text"] = note.get_text()
                n["date_of_change"] = note.get_date_of_change()
        self.__set_table(data)

    def remove_note_by_id(self, id: int) -> bool:
        data: dict = self.__get_table()
        notes_data: list = data.get("notes")
        for i in range(len(notes_data)):
            if notes_data[i].get("note_id") == id:
                notes_data.pop(i)
                self.__set_table(data)
                return True
        return False

    def remove_all_notes(self):
        data: dict = self.__get_table()
        notes_data: list = data.get("notes")
        notes_data.clear()
        self.__set_table(data)


    def add_note(self, note: Note):
        data = self.__get_table()
        data["max_id"] = data.get("max_id") + 1
        data.get('notes').append({"note_id": data.get("max_id"),
                                  "title": note.get_title(),
                                  "text": note.get_text(),
                                  "date_of_change": note.get_date_of_change()})
        self.__set_table(data)

    def __get_table(self) -> dict:
        data: dict = {}
        with open(self.__db_path, "r") as read_file:
            data = json.load(read_file)
        return data

    def __set_table(self, notes: dict):
        with open(self.__db_path, 'w') as write_file:
            json.dump(notes, write_file, indent=4)