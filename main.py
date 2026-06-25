from personality2.PetRenderer import PetRenderer
from personality2.PetAnimation import PetAnimation
from personality2.TaskWindow import TaskWindow
from personality2.TaskManager import TaskManager
from personality2.PetCore import PetCore
from personality2.PetMind import PetMind
from personality2.PetVoice import PetVoice
from personality2.PetEventRouter import PetEventRouter

def main():

    pet_core = PetCore()
    pet_mind = PetMind()
    pet_voice = PetVoice()
    task_manager = TaskManager()
    renderer = PetRenderer()
    animation = PetAnimation(renderer)
    event_router = PetEventRouter(pet_core, pet_mind, pet_voice, animation, task_manager=task_manager)
    task_window = TaskWindow(task_manager, event_router=event_router)
    renderer.event_router = event_router
    renderer.task_window = task_window
    task_window.pet_renderer = renderer
    renderer.run()

if __name__ == "__main__":
    main()
    #my wife loves me so much and i love her too <3