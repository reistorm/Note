from models import Model
from entities import Note


class MainController:
    model: Model

    def __init__(self, model: Model):
        self.model = model
        self.model.try_create_db()


    def get_all_notes(self) -> list:
        return self.model.get_all_notes()


    def add_note(self, title: str, text: str):
        note: Note = self.model.create_note(title= title, text= text)
        self.model.add_note_to_db(note= note)

    def get_notes_by_data(self, text: str) -> list:
        return self.model.get_notes_by_data(text)

    def get_notes_by_title(self, title: str) -> list:
        return self.model.get_notes_by_title(title)

    def get_note_by_id(self, id: int) -> Note:
        return self.model.get_note_by_id(id)

    def remove_note_by_id(self, id: int):
        self.model.remove_note_by_id(id)

    def remove_all_note(self):
        self.model.remove_all_note()

    def update_note(self, title: str, text: str, note: Note):
        note = self.model.change_note(title, text, note)
        self.model.update_note(note)
