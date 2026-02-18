import pygame
import sys
import os
import win32gui
import win32con
import win32api

os.environ['SDL_VIDEO_WINDOW_POS'] = '600,958'

pygame.init()

#Window settings
WIDTH, HEIGHT = 64, 64
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("QuestPet")

#Set the window to be always on top
hwnd = pygame.display.get_wm_info()['window']
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

#Make the window transparent
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
#Set the color key to magenta (255, 0, 255) and make it fully transparent
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(255,0,255), 0, win32con.LWA_COLORKEY)



clock = pygame.time.Clock()

idle_frames = []

for i in range(0, 3):
    idle_frame = pygame.image.load(f"visuals/assets/idle/i_blob_{i}.png").convert_alpha()
    idle_frames.append(idle_frame)

frame_index = 0

running = True
while running:
    for event in pygame.event.get():

        #Windows close button
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
    
    #Clear the screen
    screen.fill((255, 0, 255))  # Use magenta as the transparent color

    #Draw the idle animation
    screen.blit(idle_frames[frame_index], (1, 1))

    #Advance animation
    frame_index += 1
    if frame_index >= len(idle_frames):
        frame_index = 0

    pygame.display.update()
    clock.tick(5)

pygame.quit()
sys.exit()