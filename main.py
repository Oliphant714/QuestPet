import tkinter as tk

class Task:
    def __init__(self, description, xp_reward):
        self.description = description
        self.xp_reward = xp_reward
        self.completed = False

    def mark_complete(self):
        self.completed = True

class Dragon:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 100
        
        #Core Stats
        self.strength = 1
        self.dexterity = 1
        self.intelligence = 1
        self.charisma = 1
        self.growthpoints = 0
        self.stage = "Hatchling"

    def gain_xp(self, amount):
        self.xp += amount

        if self.xp >= self.xp_to_next_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        
        self.xp = self.xp - self.xp_to_next_level
        self.xp_to_next_level = int(self.xp_to_next_level * 1.5)
        self.award_growth_points()
        self.update_stage()

    def award_growth_points(self):
        self.growthpoints += 1  # 1 growth point per level
        if self.level == 4:
            self.growthpoints += 2
        elif self.level == 7:
            self.growthpoints += 4

    def update_stage(self):
        if self.level >= 7:
            self.stage = "Young Dragon"
        elif self.level >= 4:
            self.stage = "Wyrmling"
        else:
            self.stage = "Hatchling"

    def get_status_text(self):
        return (
            f"🐉 {self.name} the Dragon\n"
            f"Level: {self.level} ({self.stage})\n"
            f"XP: {self.xp} / {self.xp_to_next_level}"
        )

# - - - Task Lists ---
active_tasks = [
    Task("Math Homework", 25),
    Task("English Essay", 50),
    Task("Study Biology", 30)
]

completed_tasks = []


# --- Create Dragon ---
dragon = Dragon("Ember")

# --- Create Window ---
window = tk.Tk()
window.title("QuestPet")
active_label = tk.Label(window, text="Active Quests")
active_label.pack()

active_listbox = tk.Listbox(window, width=40, height=6)
active_listbox.pack(pady=5)

completed_label = tk.Label(window, text="Completed Quests")
completed_label.pack()

completed_listbox = tk.Listbox(window, width=40, height=6)
completed_listbox.pack(pady=5)

# --- Initial Task Display ---
def refresh_active_tasks():
    active_listbox.delete(0, tk.END)
    for task in active_tasks:
        active_listbox.insert(tk.END, task.description)

refresh_active_tasks()

# --- Refresh Completed Tasks ---
def refresh_completed_tasks():
    completed_listbox.delete(0, tk.END)
    for task in completed_tasks:
        completed_listbox.insert(tk.END, task.description)


# --- Label to Show Dragon Info ---
status_label = tk.Label(window, text=dragon.get_status_text(), font=("Arial", 12))
status_label.pack(pady=10)


# # --- Button Action ---
def complete_task():
    selection = active_listbox.curselection()
    if not selection:
        print("No task selected.")
        return

    index = selection[0]
    task = active_tasks[index]

    task.mark_complete()
    dragon.gain_xp(task.xp_reward)

    active_tasks.remove(task)
    completed_tasks.append(task)

    refresh_active_tasks()
    refresh_completed_tasks()

    status_label.config(text=dragon.get_status_text())



# --- Button ---
xp_button = tk.Button(window, text="Complete Task", command=complete_task)
xp_button.pack(pady=10)

# --- Start App ---
window.mainloop()
