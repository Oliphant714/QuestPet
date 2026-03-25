# from Personality import Dragon
# from Personality import UserState
# from Personality import Task

import personality2.PetRenderer as PetRenderer
from personality2.PetRenderer import PetRenderer

import personality2.PetAnimation as PetAnimation
from personality2.PetAnimation import PetAnimation

import personality2.TaskWindow as TaskWindow
from personality2.TaskWindow import TaskWindow

import personality2.Task as Task
from personality2.Task import Task

import personality2.TaskManager as TaskManager
from personality2.TaskManager import TaskManager

def main():

    renderer = PetRenderer()
    task_window = TaskWindow()
    task_window.pet_renderer = renderer
    animation = PetAnimation(renderer)
    renderer.task_window = task_window
    renderer.run()

if __name__ == "__main__":
    main()