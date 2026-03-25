from datetime import datetime

class TaskManager:
    def __init__(self):
        self.active_tasks = []
        self.completed_tasks = []
        self.streak = 0
        self.last_completion_date = None

    def add_task(self, title, description, difficulty="medium", due=None, xp_reward=20):
        task = Task(title, description, difficulty, due, xp_reward)
        self.active_tasks.append(task)
        return task

    def get_active_tasks(self):
        return self.active_tasks

    def get_completed_tasks(self):
        return self.completed_tasks

    def find_task(self, task_id):
        for t in self.active_tasks + self.completed_tasks:
            if t.task_id == task_id:
                return t
        return None

    def complete_task(self, task_id):
        task = self.find_task(task_id)
        if not task or task.completed:
            return None
        if task in self.active_tasks:
            task.mark_complete()
            self.active_tasks.remove(task)
            self.completed_tasks.append(task)
            xp = self.award_xp(task)
            self.update_streak()
        return xp

    def update_streak(self):
        today = datetime.now().date()
        if self.last_completion_date == today:
            return

        if self.last_completion_date == today.replace(day=today.day - 1):
            self.streak += 1
        else:
            self.streak = 1

        self.last_completion_date = today
    
    def award_xp(self, task):
        urgency_bonus = 0
        if self.due:
            hours_left = (self.due - datetime.now()).total_seconds() / 3600
            if hours_left < 24:
                urgency_bonus = 10
            elif hours_left < 72:
                urgency_bonus = 5

        streak_modifier = self.streak // 7
        streak_bonus = streak_modifier * 5

        return base + urgency_bonus + streak_bonus