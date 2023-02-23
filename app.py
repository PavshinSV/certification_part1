import controller
import get_choice

controller.import_notes()

while (True):
    print("1. Создать заметку.")
    print("2. Отобразить все заметки.")
    print("3. Вывести заметки в диапазоне дат.")
    print("4. Редактировать заметку.")
    print("5. Удалить заметку.")
    print("6. Импортировать заметки.")
    print("7. Экспортировать заметки.")
    choice = input("Введите номер пункта меню: ")
    get_choice.get_choice(choice)