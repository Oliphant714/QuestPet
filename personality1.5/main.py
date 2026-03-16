# from Personality import Dragon
# from Personality import UserState
# from Personality import Task

import pygame

from PetRenderer import PetRenderer
from PetAnimation import PetAnimation

def main():
    
    pet_renderer = PetRenderer()
    pet_animation = PetAnimation(pet_renderer)

    # Example usage
    pet_animation.idle()  # Start with idle animation

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pet_renderer.update()
        pet_renderer.clock.tick(10)  # Control animation speed

if __name__ == "__main__":
    main()