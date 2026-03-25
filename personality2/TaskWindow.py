import tkinter as tk
# from tkinter import *
import threading
from datetime import datetime

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

    def add_task(self):
        popup = tk.Toplevel(self.window)
        popup.title("Add Task")
        popup.geometry("300x200")

        tk.Label(popup, text="Title").pack(pady=5)
        title_entry = tk.Entry(popup)
        title_entry.pack(pady=5)

        tk.Label(popup, text="Description").pack(pady=5)
        description_entry = tk.Entry(popup)
        description_entry.pack(pady=5)

        tk.Label(popup, text="Difficulty").pack(pady=5)
        difficulty_var = tk.StringVar(value="Easy")
        difficulty_dropdown = tk.OptionMenu(popup, difficulty_var, "Easy", "Medium", "Hard")
        difficulty_dropdown.pack(pady=5)

        tk.Label(popup, text="Due Date (YYYY-MM-DD)").pack(pady=5)
        due_date_entry = tk.Entry(popup)
        due_date_entry.pack(pady=5)

        def save_task():
            title = title_entry.get()
            description = description_entry.get()
            difficulty = difficulty_var.get().lower()
            due_date_str = due_date_entry.get()
            due_date = None
            if due_date_str:
                try:
                    due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
                except ValueError:
                    tk.messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format.")
                    return

            self.task_manager.add_task(title, description, difficulty, due_date)
            self.refresh()
            popup.destroy()
        save_button = tk.Button(popup, text="Save", command=save_task)
        save_button.pack(pady=10)

    def complete_task(self):
        selected = self.active_listbox.curselection()
        if not selected:
            tk.messagebox.showwarning("No Selection", "Please select a task to complete.")
            return
        index = selected[0]
        task = self.task_manager.active_tasks[index]
        
        self.task_manager.complete_task(task.id)
        self.refresh()

    def delete_task(self):
        selected = self.active_listbox.curselection()
        if not selected:
            tk.messagebox.showwarning("No Selection", "Please select a task to delete.")
            return
        index = selected[0]
        task = self.task_manager.active_tasks[index]
        
        self.task_manager.active_tasks.remove(task)
        self.refresh()

    def edit_task(self):
        selected = self.active_listbox.curselection()
        if not selected:
            tk.messagebox.showwarning("No Selection", "Please select a task to edit.")
            return
        index = selected[0]
        task = self.task_manager.active_tasks[index]

        popup = tk.Toplevel(self.window)
        popup.title("Edit Task")
        popup.geometry("300x200")

        tk.Label(popup, text="Title").pack(pady=5)
        title_entry = tk.Entry(popup)
        title_entry.insert(0, task.title)
        title_entry.pack(pady=5)

        tk.Label(popup, text="Description").pack(pady=5)
        description_entry = tk.Entry(popup)
        description_entry.insert(0, task.description)
        description_entry.pack(pady=5)

        tk.Label(popup, text="Difficulty").pack(pady=5)
        difficulty_var = tk.StringVar(value=task.difficulty.capitalize())
        difficulty_dropdown = tk.OptionMenu(popup, difficulty_var, "Easy", "Medium", "Hard")
        difficulty_dropdown.pack(pady=5)

        tk.Label(popup, text="Due Date (YYYY-MM-DD)").pack(pady=5)
        due_date_entry = tk.Entry(popup)
        if task.due:
            due_date_entry.insert(0, task.due.strftime("%Y-%m-%d"))
        due_date_entry.pack(pady=5)

        def save_changes():
            task.title = title_entry.get()
            task.description = description_entry.get()
            task.difficulty = difficulty_var.get().lower()
            due_date_str = due_date_entry.get()
            if due_date_str:
                try:
                    task.due = datetime.strptime(due_date_str, "%Y-%m-%d")
                except ValueError:
                    tk.messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format.")
                    return
            else:
                task.due = None

            self.refresh()
            popup.destroy()
        
        save_button = tk.Button(popup, text="Save Changes", command=save_changes)
        save_button.pack(pady=10)

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