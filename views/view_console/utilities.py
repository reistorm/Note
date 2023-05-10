from .menu import Menu
from entities import Note

class Utilities:

    def request_save(self, title: str, text: str) -> bool:
        prenote: str = f'title: {title}\ntext:{text}'
        while True:
            self.show_text('Предварительный просмотр заметки')
            self.show_text(prenote)
            self.show_text(Menu.prenote_menu)
            answer: int = self.get_number(min=0, max=2)
            if answer == 0:
                return False
            elif answer == -1:
                self.show_error()
                continue
            elif answer == 1:
                return True


    def show_text(self, text):
        print(text)

    def get_number(self, min: int, max: int = None) -> int:
            answer = input()
            if answer.isdigit():
                answer = int(answer)
                if max == None and min <= answer:
                    return answer
                elif min <= answer <= max:
                    return answer
            return -1


    def show_error (self):
        print("Вы ввели некорректное значение")


    def show_notes_list(self, list):
        for n in list:
            self.show_text(n.to_string())
        input("для продолжения нажмите Enter")