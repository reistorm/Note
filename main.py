from controllers import MainController
from data import DbRequests
from models import Model
from views import View



if __name__ == '__main__':
    path = 'data\database_json\database_note.json'
    db = DbRequests(path)
    model = Model(db=db)
    controller = MainController(model=model)
    view = View(controller)

    view.run_main_menu()
