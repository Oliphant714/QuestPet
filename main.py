# from Personality import Dragon
# from Personality import UserState
# from Personality import Task

from turtle import speed

import pygame

import personality2.PetRenderer as PetRenderer
from personality2.PetRenderer import PetRenderer
import win32gui
import win32con

class QuestPet:
    def __init__(self):
        self.pet_renderer = PetRenderer()
        self.current_state = "idle"

def main():
    pygame.init()

    quest_pet = QuestPet()
    pet_renderer = quest_pet.pet_renderer

    running = True
    while running:
        for event in pygame.event.get():

            #Windows close button
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

        #Clear the screen
        pet_renderer.screen.fill((255, 0, 255))  # Use magenta as the transparent color

        #Draw the current animation
        pet_renderer.screen.blit(pet_renderer.animations[pet_renderer.current_animation][pet_renderer.frame_index], (0, 0))

        #Advance animation
        pet_renderer.frame_index = (pet_renderer.frame_index + 1) % len(pet_renderer.animations[pet_renderer.current_animation])

        if pet_renderer.frame_index >= len(pet_renderer.animations[pet_renderer.current_animation])-1:
            if pet_renderer.current_state == "idle_to_sleeping":
                pet_renderer.current_state = "sleeping"
            elif pet_renderer.current_state == "sleeping_to_idle":
                pet_renderer.frame_index = 0
                pet_renderer.current_state = "idle"
            elif pet_renderer.current_state == "walking_left":
                pet_renderer.x -= pet_renderer.speed
            elif pet_renderer.current_state == "walking_right":
                pet_renderer.x += pet_renderer.speed

        # Update window position
        win32gui.SetWindowPos(pet_renderer.hwnd, win32con.HWND_TOPMOST, int(pet_renderer.x), int(pet_renderer.y), 0, 0, win32con.SWP_NOSIZE)

        pygame.display.flip()
        pet_renderer.clock.tick(5)

if __name__ == "__main__":
    main()