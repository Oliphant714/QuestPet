from datetime import datetime
from datetime import timezone

class Task:
    next_id = 1

    def __init__(self, title, description, difficulty="medium", due=None, xp_reward=None):
        self.id = Task.next_id
        Task.next_id += 1
        self.title = title
        self.description = description
        self.difficulty = difficulty
        self.due = due  # datetime or None
        self.xp_reward = xp_reward if xp_reward is not None else self.calculate_xp(difficulty)
        self.completed = False
        self.completed_at = None

    def mark_complete(self):
        self.completed = True
        self.completed_at = datetime.now()

    def calculate_xp(self, difficulty):
        base = {"easy": 10, "medium": 20, "hard": 40}[difficulty.lower()]
        return base

    def is_overdue(self, now=None):
        if self.completed or self.due is None:
            return False
        now = now or datetime.now()
        return self.due < now

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "difficulty": self.difficulty,
            "due": self.due.isoformat() if self.due else None,
            "xp_reward": self.xp_reward,
            "completed": self.completed,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
        }

    @classmethod
    def from_dict(cls, data):
        due = datetime.fromisoformat(data["due"]) if data.get("due") else None
        task = cls(
            data["title"],
            data.get("description", ""),
            data.get("difficulty", "medium"),
            due,
            data.get("xp_reward"),
        )
        task.id = data.get("id", task.id)
        task.completed = data.get("completed", False)
        completed_at = data.get("completed_at")
        task.completed_at = datetime.fromisoformat(completed_at) if completed_at else None
        return task