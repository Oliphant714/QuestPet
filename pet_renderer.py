import pygame
import sys

pygame.init()

#Window settings
WIDTH, HEIGHT = 320, 320
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("QuestPet")

clock = pygame.time.Clock()

idle_frames = []

for i in range(1, 4):
    idle_frame = pygame.image.load(f"Visuals/assets/idle/i_{i}_blob.png").convert_alpha()
    idle_frames.append(idle_frame)

frame_index = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Clear the screen
    screen.fill((0, 0, 0))

    #Draw the idle animation
    screen.blit(idle_frames[frame_index](0, 0))

    #Advance animation
    frame_index += 1
    if frame_index >= len(idle_frames):
        frame_index = 0

    pygame.display.update()
    clock.tick(5)

pygame.quit()
sys.exit()