# from Personality import Dragon
# from Personality import UserState
# from Personality import Task

import personality2.PetRenderer as PetRenderer
from personality2.PetRenderer import PetRenderer

import personality2.PetAnimation as PetAnimation
from personality2.PetAnimation import PetAnimation

import personality2.TaskWindow as TaskWindow
from personality2.TaskWindow import TaskWindow

def main():

    renderer = PetRenderer()
    task_window = TaskWindow()
    animation = PetAnimation(renderer)
    renderer.task_window = task_window
    renderer.run()

if __name__ == "__main__":
    main()