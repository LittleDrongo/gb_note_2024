import os
import json
import datetime


class Note:
    def __init__(note, title, body):
        note.title = title
        note.body = body
        note.created_at = datetime.datetime.now()
        note.last_modified = note.created_at

        def serialize(note):
            return {
                "title": note.title,
                "created_at": note.created_at_strftime("%Y-%m-%d %H:%M:%S"),
                "body": note.body,
                "last_modified": note.last_modified.strftime("%Y-%m-%d %H:%M:%S")
            }
        
        @classmethod
        def deserialize(cls, data):
            return cls(data["title"], data["body"])
        
        def update(note, title, body):
            note.title = title
            note.body = body
            note.last_modifed = datetime.datetime.now()