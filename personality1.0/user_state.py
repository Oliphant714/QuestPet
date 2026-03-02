class UserState:
    def __init__(self):
        self.tasks_completed = 0
        self.tasks_skipped = 0
        self.consecutive_skips = 0
        self.last_action = None
        self.idle_cycles = 0

    def record_task_complete(self):
        self.tasks_completed += 1
        self.consecutive_skips = 0
        self.idle_cycles = 0
        self.last_action = "task_complete"

    def record_skip(self):
        self.tasks_skipped += 1
        self.consecutive_skips += 1
        self.last_action = "skip"

    def record_idle(self):
        self.idle_cycles += 1
        self.last_action = "idle"

    def get_emotional_state(self):
        if self.consecutive_skips >= 3:
            return "overwhelmed"
        elif self.idle_cycles >= 3:
            return "disengaged"
        elif self.tasks_completed >= 5:
            return "motivated"
        return "neutral"

    # --- Idle Thought Update ---
    # def idle_update():
    #     UserState.record_idle()
    #     message = Dragon.react("idle", UserState)
    #     if not message:
    #         message = Dragon.get_ambient_thought()
    #     message_label.config(text=message)
    #     window.after(random.randint(15000,20000), UserState.idle_update)