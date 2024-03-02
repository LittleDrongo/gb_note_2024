from note import *
import json

class NotesApp:
    def __init__(app):
        app.notes = []
        app.file_name = "notes.json"

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