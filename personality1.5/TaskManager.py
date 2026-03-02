from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.streak = 0
        self.last_completion_date = None

    def add_task(self, task):
        self.tasks.append(task)

    def get_task(self, task_id):
        for t in self.tasks:
            if t.id == task_id:
                return t
        return None

    def complete_task(self, task_id):
        task = self.get_task(task_id)
        if not task or task.completed:
            return None

        task.mark_complete()
        xp = self.calculate_xp(task)
        self.update_streak()

        return xp

    def calculate_xp(self, task):
        base = {"easy": 10, "medium": 20, "hard": 40}[task.difficulty]

        urgency_bonus = 0
        if task.due:
            hours_left = (task.due - datetime.now()).total_seconds() / 3600
            if hours_left < 24:
                urgency_bonus = 10
            elif hours_left < 72:
                urgency_bonus = 5

        streak_bonus = self.streak * 2

        return base + urgency_bonus + streak_bonus

    def update_streak(self):
        today = datetime.now().date()
        if self.last_completion_date == today:
            return

        if self.last_completion_date == today.replace(day=today.day - 1):
            self.streak += 1
        else:
            self.streak = 1

        self.last_completion_date = today