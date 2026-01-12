import tkinter as tk


class Dragon:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 100
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
        self.growthpoints += 1
        self.xp = self.xp - self.xp_to_next_level
        self.xp_to_next_level = int(self.xp_to_next_level * 1.5)
        self.update_stage()

    def update_stage(self):
        if self.level >= 7:
            self.stage = "Young Dragon"
            if self.level == 7:
                self.growthpoints += 5  # Bonus growth points on reaching Young Dragon
        elif self.level >= 4:
            self.stage = "Wyrmling"
            if self.level == 4:
                self.growthpoints += 3  # Bonus growth points on reaching Wyrmling
        else:
            self.stage = "Hatchling"

    def get_status_text(self):
        return (
            f"🐉 {self.name} the Dragon\n"
            f"Level: {self.level} ({self.stage})\n"
            f"XP: {self.xp} / {self.xp_to_next_level}"
        )


# --- Create Dragon ---
dragon = Dragon("Ember")

# --- Create Window ---
window = tk.Tk()
window.title("QuestPet")

# --- Label to Show Dragon Info ---
status_label = tk.Label(window, text=dragon.get_status_text(), font=("Arial", 12))
status_label.pack(pady=10)


# --- Button Action ---
def complete_task():
    dragon.gain_xp(25)
    status_label.config(text=dragon.get_status_text())


# --- Button ---
xp_button = tk.Button(window, text="Complete Task (+25 XP)", command=complete_task)
xp_button.pack(pady=10)

# --- Start App ---
window.mainloop()
