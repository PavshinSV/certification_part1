import controller
import datetime

notes = []
id = 0

def new_note():
    header = input("Введите описание заметки: ")
    content = input("Введите содержание заметки: ")
    controller.id += 1
    note = {
        "id": controller.id,
        "header": header,
        "content": content,
        "date": datetime.datetime.now().date().strftime("%d-%m-%Y"),
        "time": datetime.datetime.now().time().strftime("%H:%M")
    }
    print(note)
    controller.notes.append(note)
    print("------------------------------------------------")


def show_all():
    pass

def show_range(start_date,end_date):
    pass

def edit_note(id):
    pass

def remove_note(id):
    pass

def import_notes():
    pass

def export_notes():
    pass