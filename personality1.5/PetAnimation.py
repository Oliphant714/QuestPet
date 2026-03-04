class PetAnimation:
    def __init__(self, renderer):
        self.renderer = renderer
    
    def play(self, animation_name):
        self.renderer.set_state(animation_name)

    
    def idle(self):
        self.play("idle")
    def sleeping(self):
        self.play("sleeping")
    def idle_to_sleeping(self):
        self.play("idle_to_sleeping")
    def sleeping_to_idle(self):
        self.play("sleeping_to_idle")
    def walking_left(self):
        self.play("walking_left")
    def walking_right(self):
        self.play("walking_right")