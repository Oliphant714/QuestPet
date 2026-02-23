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

def load_animation(folder_path):
    frames = []
    for file in sorted(os.listdir(folder_path)):
        if file.endswith('.png'):
             frames.append(pygame.image.load(os.path.join(folder_path, file)).convert_alpha())
    return frames

animations = {
    "idle": load_animation("visuals/assets/idle"),
    "sleeping": load_animation("visuals/assets/sleeping"),
    "idle_to_sleeping": load_animation("visuals/assets/idle_to_sleeping"),
    "sleeping_to_idle": load_animation("visuals/assets/sleeping_to_idle"),
    "walking_left": load_animation("visuals/assets/walking_left"),
    "walking_right": load_animation("visuals/assets/walking_right"),
}

current_state = "idle"
current_animation = "idle"
frame_index = 0

running = True
while running:
    for event in pygame.event.get():

        #Windows close button
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
        #State changes by buttons
        elif event.type == pygame.KEYDOWN:
            if current_state != "sleeping":
                if event.key == pygame.K_a:
                    current_state = "walking_left"
                    #x -= 5
                    frame_index = 0
                elif event.key == pygame.K_d:
                    current_state = "walking_right"
                    #x += 5
                    frame_index = 0
                elif event.key == pygame.K_s:
                    current_state = "idle_to_sleeping"
                    frame_index = 0   
            elif current_state == "sleeping":    
                if event.key == pygame.K_w:
                    current_state = "sleeping_to_idle"
                    frame_index = 0
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_a, pygame.K_d]:
                current_state = "idle"
                frame_index = 0

    if current_state == "idle":
        current_animation = "idle"
    elif current_state == "sleeping":
        current_animation = "sleeping"
    elif current_state == "idle_to_sleeping":
        current_animation = "idle_to_sleeping"
    elif current_state == "sleeping_to_idle":
        current_animation = "sleeping_to_idle"
    elif current_state == "walking_left":
        current_animation = "walking_left"
    elif current_state == "walking_right":
        current_animation = "walking_right"

    #Clear the screen
    screen.fill((255, 0, 255))  # Use magenta as the transparent color

    #Draw the current animation
    screen.blit(animations[current_animation][frame_index], (0, 0))

    #Advance animation
    frame_index = (frame_index + 1) % len(animations[current_animation])

    if frame_index >= len(animations[current_animation])-1:
        frame_index = 0
        if current_state == "idle_to_sleeping":
            current_state = "sleeping"
        elif current_state == "sleeping_to_idle":
            current_state = "idle"

    pygame.display.flip()
    clock.tick(5)

pygame.quit()
sys.exit()