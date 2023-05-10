from data import DbRequests
from entities import Note
class ModelBasic:
    db: DbRequests

    def __init__(self, db: DbRequests):
        self.db = db
    def try_create_db(self):
        if not self.db.check_exist_table():
            self.db.create_table()


    def get_all_notes(self) -> list:
        return self.db.select_all_notes()


    def create_note(self, title: str, text: str) -> Note:
        note = Note(title= title, text= text)
        return note


    def add_note_to_db(self, note: Note):
        self.db.add_note(note= note)

    def get_notes_by_data(self, text: str) -> list:
        return self.db.select_notes_by_date(text)

    def get_notes_by_title(self, title: str) -> list:
        return self.db.select_notes_by_title(title)

    def get_note_by_id(self, id: int) -> Note:
        return self.db.select_note_by_id(id)

    def remove_note_by_id(self, id: int):
        self.db.remove_note_by_id(id= id)

    def remove_all_note(self):
        self.db.remove_all_notes()

    def change_note(self, title: str, text: str, note: Note) -> Note:
        note.set_title(title)
        note.set_text(text)
        return note

    def update_note(self, note: Note):
        self.db.update_note(note)