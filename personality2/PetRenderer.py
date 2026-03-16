import pygame
import os
import win32gui
import win32con
import win32api

class PetRenderer:
    def __init__(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = '600,958'
        pygame.init()

        self.WIDTH, self.HEIGHT = 64, 64
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.NOFRAME)
        pygame.display.set_caption("QuestPet")

        # Window setup
        self.hwnd = pygame.display.get_wm_info()['window']
        self.x, self.y = 600, 958
        self.speed = 10

        win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST, self.x, self.y, 0, 0,
                              win32con.SWP_NOSIZE | win32con.SWP_NOZORDER)

        win32gui.SetWindowLong(self.hwnd, win32con.GWL_EXSTYLE,
                               win32gui.GetWindowLong(self.hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
        win32gui.SetLayeredWindowAttributes(self.hwnd, win32api.RGB(255,0,255), 0, win32con.LWA_COLORKEY)

        self.clock = pygame.time.Clock()

        species = "blob"  # This can be made dynamic later
        self.species = species
        # Load animations
        self.animations = {
            "idle": self.load_animation(f"visuals/assets/{self.species}/idle"),
            "sleeping": self.load_animation(f"visuals/assets/{self.species}/sleeping"),
            "idle_to_sleeping": self.load_animation(f"visuals/assets/{self.species}/idle_to_sleeping"),
            "sleeping_to_idle": self.load_animation(f"visuals/assets/{self.species}/sleeping_to_idle"),
            "walking_left": self.load_animation(f"visuals/assets/{self.species}/walking_left"),
            "walking_right": self.load_animation(f"visuals/assets/{self.species}/walking_right")#,
            # "happy": self.load_animation(f"visuals/assets/{self.species}/happy"),  # add new animations easily
            # "level_up": self.load_animation(f"visuals/assets/{self.species}/level_up")
        }

        self.current_state = "idle"
        self.current_animation = "idle"
        self.frame_index = 0

    def load_animation(self, folder_path):
        frames = []
        for file in sorted(os.listdir(folder_path)):
            if file.endswith('.png'):
                frames.append(pygame.image.load(os.path.join(folder_path, file)).convert_alpha())
        return frames

    def set_state(self, new_state):
        self.current_state = new_state
        self.frame_index = 0

    def update(self):
        # Advance animation
        frames = self.animations[self.current_state]
        self.frame_index = (self.frame_index + 1) % len(frames)

        # Movement logic
        if self.current_state == "walking_left":
            self.x -= self.speed
        elif self.current_state == "walking_right":
            self.x += self.speed

        win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST, int(self.x), int(self.y), 0, 0,
                              win32con.SWP_NOSIZE)

    def draw(self):
        self.screen.fill((255, 0, 255))
        frame = self.animations[self.current_state][self.frame_index]
        self.screen.blit(frame, (0, 0))
        pygame.display.flip()
        self.clock.tick(5)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.update()
            self.draw()

        pygame.quit()