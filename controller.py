import controller
import datetime
import json

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
    if len(notes) == 0:
        print("Сообщения отсутствуют!")
        print("------------------------------------------------")
    else:
        for note in notes:
            print(note)
        print("------------------------------------------------")


def show_range(start_date, end_date):
    pass


def edit_note(id):
    pass


def remove_note(id):
    pass


def import_notes():
    try:
        with open("data.json", "r") as fr:
            controller.notes = json.load(fr)
            last_note = controller.notes[len(controller.notes) - 1]
            controller.id = last_note["id"]
    except Exception:
        print("Упс! Ошибка чтения! Проверьте носитель/наличие файла и повторите попытку")
        print("------------------------------------------------")


def export_notes():
    try:
        with open("data.json", "w") as fw:
            json.dump(controller.notes, fw)
    except Exception:
        print("Упс! Ошибка записи! Проверьте носитель и повторите попытку")
        print("------------------------------------------------")