class PetEventRouter:
    def __init__(self, pet_core, pet_mind, pet_voice, pet_animation, task_manager=None):
        self.core = pet_core
        self.mind = pet_mind
        self.voice = pet_voice
        self.anim = pet_animation
        self.task_manager = task_manager

    def get_mode(self):
        return self.mind.get_mode()

    def get_mode_display(self):
        return self.mind.describe_mode()

    def set_mode(self, mode):
        return self.mind.set_mode(mode, manual=True, reason="user selected mode")

    def set_auto_mode(self):
        return self.mind.set_auto_mode(reason="user selected auto mode")

    def _animation_for_mode(self, mode, event_name):
        normalized_mode = (mode or "observe").lower()
        animation_map = {
            "task_complete": {
                "play": "walking_right",
                "assist": "walking_left",
                "observe": "idle",
            },
            "level_up": {
                "play": "walking_right",
                "assist": "walking_left",
                "observe": "idle",
            },
            "idle": {
                "play": "idle",
                "assist": "idle",
                "observe": "idle",
            },
            "overdue": {
                "play": "walking_left",
                "assist": "walking_left",
                "observe": "idle",
            },
        }
        return animation_map.get(event_name, {}).get(normalized_mode, "idle")

    def _play_animation(self, animation_name):
        if self.anim is not None:
            self.anim.play(animation_name)

    def on_task_completed(self, xp, task=None):
        leveled_up = self.core.gain_xp(xp)

        mode = self.mind.on_task_complete(task=task, task_manager=self.task_manager)
        event_name = "level_up" if leveled_up else "task_complete"
        self._play_animation(self._animation_for_mode(mode, event_name))

        task_name = getattr(task, "title", "task")
        return self.voice.get_line(event_name, mode, {"task_title": task_name})

    def on_idle(self):
        mode = self.mind.on_idle(task_manager=self.task_manager)
        self._play_animation(self._animation_for_mode(mode, "idle"))
        return self.voice.get_line("idle", mode)

    def on_overdue_task(self, task=None):
        mode = self.mind.on_overdue_task(task=task, task_manager=self.task_manager)
        self._play_animation(self._animation_for_mode(mode, "overdue"))
        task_name = getattr(task, "title", "task")
        return self.voice.get_line("overdue", mode, {"task_title": task_name})