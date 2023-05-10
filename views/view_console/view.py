from controllers import MainController
from .menu import Menu
from entities import Note
from .utilities import Utilities

class ViewConsoleBasic:
    main_menu_dict: dict
    controller: MainController
    menu: Menu
    util: Utilities

    def __init__(self, controller: MainController):
        self.controller = controller
        self.menu = Menu()
        self.util = Utilities()
        self.main_menu_dict = {1: self.show_all_notes,
                               2: self.run_select_menu,
                               3: self.run_add_menu,
                               4: self.run_update,
                               5: self.run_remove_menu}


    def run_main_menu(self):
        while True:
            self.util.show_text(self.menu.main_menu)
            answer: int = self.util.get_number(min=0, max=5)
            if answer == 0:
                return
            elif answer == -1:
                self.util.show_error()
                continue
            else:
                self.main_menu_dict.get(answer)()


    def show_all_notes(self):
        notes_list: list = self.controller.get_all_notes()
        if notes_list == []:
            self.util.show_text("Заметки отсутствуют")
        self.util.show_notes_list(list= notes_list)


    def run_select_menu(self):
        text: str = ''
        num: int = 0
        notes_list: list
        while True:
            notes_list = []
            self.util.show_text(self.menu.select_menu)
            answer: int = self.util.get_number(min=0, max=3)
            if answer == 0:
                return
            elif answer == -1:
                self.util.show_error()
                continue
            elif answer == 1:
                self.util.show_text("Введите Id")
                num = self.util.get_number(min= 1)
                if num != -1:
                    notes_list.append(self.controller.get_note_by_id(id= num))
            elif answer == 2:
                text = input("Введите дату или часть даты в формате д.м.г-ч:м:с например 28.02 или 02.2023\n")
                notes_list = self.controller.get_notes_by_data(text=text)
            elif answer == 3:
                text = input("Введите заголовок или его часть\n").lower()
                notes_list = self.controller.get_notes_by_title(title=text)
            if text == "" and num == 0:
                self.util.show_text('Запрос отсутсвует')
            elif notes_list == []:
                self.util.show_text("Заметки отсутствуют")
            else:
                self.util.show_notes_list(list= notes_list)


    def run_remove_menu(self):
        num: int = 0
        while True:
            self.util.show_text(self.menu.remove_menu)
            answer: int = self.util.get_number(min=0, max=2)
            if answer == 0:
                return
            elif answer == -1:
                self.util.show_error()
                continue
            elif answer == 1:
                self.util.show_text("Введите Id")
                num = self.util.get_number(min=1)
                if num != -1:
                    note = self.controller.get_note_by_id(id=num)
                    if note.get_id() == 0:
                        self.util.show_text('Заметка с таким Id не существует')
                    else:
                        if self.util.request_save(title=note.get_title(), text=note.get_text()):
                            self.controller.remove_note_by_id(id= note.get_id())
            elif answer == 2:
                self.util.show_text(self.menu.prenote_menu)
                answer: int = self.util.get_number(min=0, max=1)
                if answer == 0 or answer == -1:
                    continue
                else:
                    self.controller.remove_all_note()


    def run_update(self):
        num: int = 0
        while True:
            self.util.show_text("Введите Id заметки или 0 для возврата в меню")
            answer: int = self.util.get_number(min=0)
            if answer == 0:
                return
            elif answer == -1:
                self.util.show_error()
                continue
            else:
                note = self.controller.get_note_by_id(id=answer)
                if note.get_id() == 0:
                    self.util.show_text('Заметка с таким Id не существует')
                else:
                    self.run_update_menu(note)

    def run_update_menu(self, note: Note):
        title: str = note.get_title()
        text: str = note.get_text()
        while True:
            self.util.show_text(self.menu.update_menu)
            answer: int = self.util.get_number(min=0, max=3)
            if answer == 0:
                return
            elif answer == -1:
                self.util.show_error()
                continue
            elif answer == 1:
                title = input("Введите текст заголовка\n")
            elif answer == 2:
                text = input("Введите текст заметки\n")
            elif answer == 3:
                if self.util.request_save(title= title, text= text):
                    self.controller.update_note(title= title, text= text, note= note)
                    return


    def run_add_menu(self):
        title: str = 'Нет заголовка'
        text: str = 'Нет текста заметки'
        while True:
            self.util.show_text(self.menu.add_menu)
            answer: int = self.util.get_number(min=0, max=3)
            if answer == 0:
                return
            elif answer == -1:
                self.util.show_error()
                continue
            elif answer == 1:
                title = input("Введите текст заголовка\n")
            elif answer == 2:
                text = input("Введите текст заметки\n")
            elif answer == 3:
                if self.util.request_save(title= title, text= text):
                    self.controller.add_note(title=title, text=text)
