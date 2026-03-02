class PetCore:
    def __init__(self):
        self.level = 1
        self.xp = 0
        self.xp_to_next = 100
        self.growth_points = 0

    def gain_xp(self, amount):
        self.xp += amount
        leveled_up = False

        while self.xp >= self.xp_to_next:
            self.xp -= self.xp_to_next
            self.level_up()
            leveled_up = True

        return leveled_up

    def level_up(self):
        self.level += 1
        self.xp_to_next = int(self.xp_to_next * 1.5)
        self.growth_points += 1