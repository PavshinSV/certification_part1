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
    try:
        start = datetime.datetime.strptime(start_date, "%d-%m-%Y")
        stop = datetime.datetime.strptime(end_date, "%d-%m-%Y")
        if start > stop:
            temp = stop
            stop = start
            start = temp
        no_elements = True
        for element in controller.notes:
            date = datetime.datetime.strptime(element["date"], "%d-%m-%Y")
            if start <= date <= stop:
                no_elements = False
                print(element)
        if no_elements:
            print("Записки в указанном диапазоне дат отсутствуют")
        print("------------------------------------------------")
    except Exception:
        print("Формат ввода даты не соответствует требуемому!")
        print("------------------------------------------------")


def edit_note(note_id):
    pass


def remove_note(note_id):
    if id == "0" or len(controller.notes) == 0:
        return
    try:
        note_id = int(note_id)
        removed = False
        for element in notes:
            if element["id"] == note_id:
                notes.remove(element)
                print(f"Заметка {element} успешно удалена")
                removed = True
                break
        if not removed:
            print("Заметки с указанным id не найдено")
    except Exception:
        print("Ошибка ввода, введенное значение должно быть положительным целым числом")


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
    if len(controller.notes) > 0:
        try:
            with open("data.json", "w") as fw:
                json.dump(controller.notes, fw)
        except Exception:
            print("Упс! Ошибка записи! Проверьте носитель и повторите попытку")
            print("------------------------------------------------")
    else:
        print("Отсутствуют заметки для экспорта")
        print("------------------------------------------------")
