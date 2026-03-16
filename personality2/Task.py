from uuid import uuid4
from datetime import datetime

class Task:
    def __init__(self, title, source, difficulty="medium", due=None):
        self.id = uuid4()
        self.title = title
        self.source = source  # "canvas", "user", "pet"
        self.difficulty = difficulty
        self.due = due  # datetime or None
        self.completed = False
        self.completed_at = None

    def mark_complete(self):
        self.completed = True
        self.completed_at = datetime.now()