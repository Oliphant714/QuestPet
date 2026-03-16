class PetEventRouter:
    def __init__(self, pet_core, pet_mind, pet_voice, pet_animation):
        self.core = pet_core
        self.mind = pet_mind
        self.voice = pet_voice
        self.anim = pet_animation

    def on_task_completed(self, xp):
        leveled_up = self.core.gain_xp(xp)

        if leveled_up:
            self.mind.on_level_up()
            self.anim.play("level_up")
            return self.voice.get_line("level_up")

        self.mind.on_task_complete()
        self.anim.play("happy")
        return self.voice.get_line("task_complete")

    def on_idle(self):
        self.mind.on_idle()
        self.anim.play("idle_fidget")
        return self.voice.get_line("idle")

    def on_overdue_task(self):
        self.mind.on_overdue()
        self.anim.play("concerned")
        return self.voice.get_line("overdue")