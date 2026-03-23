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

        label = tk.Label(self.window, text="Your Tasks")
        label.pack(pady=20)

        close_button = tk.Button(self.window, text="Close", command=self.close)
        close_button.pack(pady=10)

        self.active_listbox = tk.Listbox(self.window)
        self.active_listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.window.mainloop()

    def refresh(self):
        self.active_listbox.delete(0, tk.END)
        for task in self.task_manager.active_tasks:
            self.active_listbox.insert(tk.END, f"{task.id}: {task.title} - {task.difficulty}")

    def close(self):
        if self.window:
            self.window.destroy()
            self.window = None

    