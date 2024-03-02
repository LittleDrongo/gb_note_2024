from note import *
from const import *
import json

class NotesApp:
    def __init__(app):
        app.notes = []
        app.file_name = DATAFILE

    def load_notes(app):
        if os.path.exists(app.file_name):
            with open(app.file_name, "r") as file:
                data = json.load(file)
                app.notes = [Note.deserialize(note_data) for note_data in data]

    def save_notes(app):
        with open(app.file_name, "w") as file:
            data = [note.serialize() for note in app.notes]
            json.dump(data, file, indent=4)

    def add_note(app, title, body):
        note = Note(title, body)
        app.notes.append(note)
        app.save_notes()

    def edit_note(app, index, title, body):
        if 0 <= index < len(app.notes):
            app.notes[index].update(title, body)
            app.save_notes()
            print("Заметка успешно отредактирована.")
        else:
            print("Недопустимый индекс заметки.")

    def delete_note(app, index):
        if 0 <= index < len(app.notes):
            del app.notes[index]
            app.save_notes()
            print("Заметка успешно удалена.")
        else:
            print("Недопустимый индекс заметки.")

    def list_notes(app, filter_date=None):
        for i, note in enumerate(app.notes):
            if filter_date is None or note.created_at.date() == filter_date.date():
                print(f"{i}: {note.title} - {note.created_at}")

    def run_menu(app):
        app.load_notes()
        while True:
            print()
            print("\nВыберите действие:")
            print("1. Показать все заметки")
            print("2. Добавить новую заметку")
            print("3. Редактировать заметку")
            print("4. Удалить заметку")
            print("5. Выход")
            choice = input("Введите номер действия: ")

            if choice == "1":
                app.list_notes()
            elif choice == "2":
                title = input("Введите заголовок заметки: ")
                body = input("Введите текст заметки: ")
                app.add_note(title, body)
            elif choice == "3":
                index = int(input("Введите номер заметки для редактирования: "))
                title = input("Введите новый заголовок заметки: ")
                body = input("Введите новый текст заметки: ")
                app.edit_note(index, title, body)
            elif choice == "4":
                index = int(input("Введите номер заметки для удаления: "))
                app.delete_note(index)
            elif choice == "5":
                break
            else:
                print("Неверный ввод, попробуйте снова.")