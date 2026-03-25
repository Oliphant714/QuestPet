from uuid import uuid4
from datetime import datetime

class Task:
    next_id = 1

    def __init__(self, title, description, difficulty="medium", due=None, xp_reward=20):
        self.id = Task.next_id
        Task.next_id += 1
        self.title = title
        self.description = description
        self.difficulty = difficulty
        self.due = due  # datetime or None
        self.xp_reward = self.calculate_xp(difficulty)  # XP reward for completing the task
        self.completed = False
        self.completed_at = None

    def mark_complete(self):
        self.completed = True
        self.completed_at = datetime.now()

    def calculate_xp(self, difficulty):
        base = {"easy": 10, "medium": 20, "hard": 40}[difficulty]
        return base