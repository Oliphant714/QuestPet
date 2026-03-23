import tkinter as tk
import threading

class TaskWindow:
    def __init__(self):
        self.window = None

    def open(self):
        if self.window is not None:
            try:
                self.window.destroy()
            except:
                pass
        threading.Thread(target=self.create_window, daemon=True).start()

    def create_window(self):
        self.window = tk.Tk()
        self.window.title("Tasks")
        self.window.geometry("400x300")
        self.window.mainloop()

        label = tk.Label(self.window, text="Your Tasks")
        label.pack(pady=20)

        self.window.mainloop()

    #     self.create_window()

    # def create_window(self):
    #     self.screen = pygame.display.set_mode((400, 300))
    #     pygame.display.set_caption("Tasks")

    # def draw(self):
    #     self.screen.fill((50, 50, 50))
    #     pygame.display.flip()
    
    # def recreate_window(self):
    #     pygame.display.quit()
    #     pygame.display.init()
    #     self.create_window()