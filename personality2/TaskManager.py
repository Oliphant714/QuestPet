from datetime import datetime
from datetime import timedelta
import json
from pathlib import Path
from personality2.Task import Task

class TaskManager:
    def __init__(self, storage_path=None):
        self.active_tasks = []
        self.completed_tasks = []
        self.streak = 0
        self.last_completion_date = None
        self.storage_path = Path(storage_path) if storage_path else Path("questpet_tasks.json")
        self.load_state()

    def add_task(self, title, description, difficulty="medium", due=None, xp_reward=None):
        task = Task(title, description, difficulty, due, xp_reward)
        self.active_tasks.append(task)
        return task

    def get_active_tasks(self):
        return self.active_tasks

    def get_completed_tasks(self):
        return self.completed_tasks

    def find_task(self, task_id):
        for t in self.active_tasks + self.completed_tasks:
            if t.id == task_id:
                return t
        return None

    def complete_task(self, task_id):
        task = self.find_task(task_id)
        if not task or task.completed:
            return 0
        if task in self.active_tasks:
            task.mark_complete()
            self.active_tasks.remove(task)
            self.completed_tasks.append(task)
            self.update_streak()
            xp = self.award_xp(task)
            return xp
        return 0

    def update_streak(self):
        today = datetime.now().date()
        if self.last_completion_date == today:
            return

        if self.last_completion_date is not None and today - self.last_completion_date == timedelta(days=1):
            self.streak += 1
        else:
            self.streak = 1

        self.last_completion_date = today
    
    def award_xp(self, task):
        base = task.xp_reward
        urgency_bonus = 0
        if task.due:
            hours_left = (task.due - datetime.now()).total_seconds() / 3600
            if hours_left < 24:
                urgency_bonus = 10
            elif hours_left < 72:
                urgency_bonus = 5

        streak_modifier = self.streak // 7
        streak_bonus = streak_modifier * 5

        return base + urgency_bonus + streak_bonus

    def get_overdue_tasks(self):
        return [task for task in self.active_tasks if task.is_overdue()]

    def save_state(self):
        payload = {
            "streak": self.streak,
            "last_completion_date": self.last_completion_date.isoformat() if self.last_completion_date else None,
            "next_task_id": Task.next_id,
            "active_tasks": [task.to_dict() for task in self.active_tasks],
            "completed_tasks": [task.to_dict() for task in self.completed_tasks],
        }
        self.storage_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def load_state(self):
        if not self.storage_path.exists():
            return

        data = json.loads(self.storage_path.read_text(encoding="utf-8"))
        self.streak = data.get("streak", 0)
        last_completion_date = data.get("last_completion_date")
        self.last_completion_date = datetime.fromisoformat(last_completion_date).date() if last_completion_date else None
        self.active_tasks = [Task.from_dict(task_data) for task_data in data.get("active_tasks", [])]
        self.completed_tasks = [Task.from_dict(task_data) for task_data in data.get("completed_tasks", [])]
        Task.next_id = max(data.get("next_task_id", Task.next_id), self._next_task_id_from_tasks())

    def _next_task_id_from_tasks(self):
        task_ids = [task.id for task in self.active_tasks + self.completed_tasks]
        return (max(task_ids) + 1) if task_ids else Task.next_id