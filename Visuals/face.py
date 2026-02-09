import os
import tkinter as tk
import random
from win32api import GetMonitorInfo, MonitorFromPoint

# --- Dragon States ---
IDLE = "idle"
SLEEPING = "sleeping"
WALKING_LEFT = "walking_left"
WALKING_RIGHT = "walking_right"
# TRANSITION = "transition"
IDLE_TO_SLEEPING = "idle_to_sleeping"
SLEEPING_TO_IDLE = "sleeping_to_idle"



monitor_info=GetMonitorInfo(MonitorFromPoint((0, 0)))
work_area=monitor_info.get('Work')
screen_width=work_area[2]
work_height=work_area[3]

class Ket:
    def __init__(self):
        self.window=tk.Tk()

        self.idle = self.load_animation("assets/idle")
        self.idle_to_sleeping = self.load_animation("assets/idle_to_sleeping")
        self.sleeping = self.load_animation("assets/sleeping")
        self.sleeping_to_idle = self.load_animation("assets/sleeping_to_idle")
        self.walking_left = self.load_animation("assets/walking_left")
        self.walking_right = self.load_animation("assets/walking_right")

        self.width = self.idle[0].width()
        self.height = self.idle[0].height()
        
        self.x=int(screen_width*0.8)
        self.y=work_height-self.height

        self.i_frame=0
        self.state=IDLE
        # self.next_state=IDLE

        self.frame=self.idle[0]

        self.window.config(highlightbackground='black')
        self.label = tk.Label(self.window,bd=0,bg='black')
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        self.window.wm_attributes('-transparentcolor','black')

        self.label.pack()

        self.window.after(50, self.update)
        self.window.mainloop()

    def load_animation(self, folder_path):
        frames = []

        for file in sorted(os.listdir(folder_path)):
            if file.endswith(".png"):
                full_path = os.path.join(folder_path, file)
                frames.append(tk.PhotoImage(file=full_path))

        return frames


    def set_state(self, new_state):
        if self.state != new_state:
            self.state = new_state
            self.i_frame = 0

    # def decide_next_state(self):
    #     roll = random.random()

    #     if roll < 0.6:
    #         self.next_state = IDLE
    #     elif roll < 0.75:
    #         self.next_state = WALKING_LEFT
    #     elif roll < 0.9:
    #         self.next_state = WALKING_RIGHT
    #     else:
    #         self.next_state = SLEEPING

    def update(self):
    
        if self.state == IDLE:
            self.frame = self.idle[self.i_frame]
            self.animate(self.idle)
        elif self.state == SLEEPING:
            self.frame = self.sleeping[self.i_frame]
            self.animate(self.sleeping)
        elif self.state == WALKING_LEFT:
            self.frame = self.walking_left[self.i_frame]
            self.animate(self.walking_left)
        elif self.state == WALKING_RIGHT:
            self.frame = self.walking_right[self.i_frame]
            self.animate(self.walking_right)
        elif self.state == IDLE_TO_SLEEPING:
            self.frame = self.idle_to_sleeping[self.i_frame]
            self.animate(self.idle_to_sleeping)
        elif self.state == SLEEPING_TO_IDLE:
            self.frame = self.sleeping_to_idle[self.i_frame]
            self.animate(self.sleeping_to_idle)
 
        self.window.geometry(f'{self.width}x{self.height}+{self.x}+{self.y}')
        self.label.configure(image=self.frame)
        self.window.after(50, self.update)

    def animate(self, frames):
        self.i_frame = (self.i_frame + 1) % len(frames)

ket=Ket()      
