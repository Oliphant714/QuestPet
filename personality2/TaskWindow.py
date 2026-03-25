import tkinter as tk
# from tkinter import *
import threading

class TaskWindow:
    def __init__(self, task_manager):
        self.window = None
        self.pet_renderer = None
        self.task_manager = task_manager

    def open(self):
        if self.window is not None:
            try:
                self.window.destroy()
            except:
                pass
        threading.Thread(target=self.create_window, daemon=True).start()

    def create_window(self):
        # task_window = TaskWindow(task_manager, event_router)
        # task_window.pet_renderer = renderer

        self.window = tk.Tk()
        self.window.title("Tasks")
        self.window.geometry("400x300")

        self.window.protocol("WM_DELETE_WINDOW", self.close)

        scroll_area = ScrollableFrame(self.window)
        scroll_area.pack(fill=tk.BOTH, expand=True)

        active_label = tk.Label(scroll_area.scrollable_frame, text="Your Tasks")
        active_label.pack(pady=20)

        add_task_button = tk.Button(scroll_area.scrollable_frame, text="Add Task", command=self.add_task)
        add_task_button.pack(pady=10)

        edit_task_button = tk.Button(scroll_area.scrollable_frame, text="Edit Task", command=self.edit_task)
        edit_task_button.pack(pady=10)

        delete_task_button = tk.Button(scroll_area.scrollable_frame, text="Delete Task", command=self.delete_task)
        delete_task_button.pack(pady=10)

        complete_task_button = tk.Button(scroll_area.scrollable_frame, text="Complete Task", command=self.complete_task)
        complete_task_button.pack(pady=10)

        active_listbox = tk.Listbox(scroll_area.scrollable_frame, width=50, height=10)
        active_listbox.pack(pady=10)

        completed_label = tk.Label(scroll_area.scrollable_frame, text="Completed Tasks")
        completed_label.pack(pady=20)

        completed_listbox = tk.Listbox(scroll_area.scrollable_frame, width=50, height=10)
        completed_listbox.pack(pady=10)

        close_button = tk.Button(scroll_area.scrollable_frame, text="Close", command=self.close)
        close_button.pack(pady=10)

        self.window.mainloop()

    def refresh(self):
        self.active_listbox.delete(0, tk.END)
        for task in self.task_manager.active_tasks:
            self.active_listbox.insert(tk.END, f"{task.id}: {task.title} - {task.difficulty}")

    def close(self):
        if self.window:
            self.window.destroy()
            self.window = None
            if self.pet_renderer:
                self.pet_renderer.bring_to_front()

class ScrollableFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")