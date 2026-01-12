class Pet:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.current_xp = 0
        self.xp_to_next_level = 100

        self.strength = 1
        self.intelligence = 1
        self.endurance = 1
        self.happiness = 5

        self.stage = "Hatchling"

    def gain_xp(self, amount):
        self.current_xp += amount
        print(f"{self.name} gained {amount} XP!")

        if self.current_xp >= self.xp_to_next_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.current_xp = self.current_xp - self.xp_to_next_level
        self.xp_to_next_level = int(self.xp_to_next_level * 1.5)

        # Increase stats
        self.strength += 1
        self.intelligence += 1
        self.endurance += 1
        self.happiness += 1

        self.update_stage()

        print(f"{self.name} leveled up to Level {self.level}!")
        print(f"Stage: {self.stage}")

    def update_stage(self):
        if self.level >= 7:
            self.stage = "Young Dragon"
        elif self.level >= 4:
            self.stage = "Wyrmling"
        else:
            self.stage = "Hatchling"

    def get_status_text(self):
        return (
            f"{self.name} the Dragon\n"
            f"Level: {self.level}\n"
            f"Stage: {self.stage}\n"
            f"XP: {self.current_xp} / {self.xp_to_next_level}\n"
            f"STR: {self.strength}  INT: {self.intelligence}  END: {self.endurance}\n"
            f"Happiness: {self.happiness}"
        )
