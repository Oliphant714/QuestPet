class PetAnimation:
    def __init__(self, renderer):
        self.renderer = renderer
    
    def play(self, animation_name):
        self.renderer.set_state(animation_name)