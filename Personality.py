import tkinter as tk
import random

class Task:
    def __init__(self, description, xp_reward):
        self.description = description
        self.xp_reward = xp_reward
        self.completed = False

    def mark_complete(self):
        self.completed = True

    # # --- Initial Task Display ---
    # def refresh_active_tasks():
    #     active_listbox.delete(0, tk.END)
    #     for task in active_tasks:
    #         active_listbox.insert(tk.END, task.description)

    # # --- Refresh Completed Tasks ---
    # def refresh_completed_tasks():
    #     completed_listbox.delete(0, tk.END)
    #     for task in completed_tasks:
    #         completed_listbox.insert(tk.END, task.description)

    # # --- Complete Task Button Action ---
    # def complete_task():
    #     selection = active_listbox.curselection()
    #     if not selection:
    #         message_label.config(text="No task selected!")
    #         return

    #     index = selection[0]
    #     task = active_tasks[index]

    #     task.mark_complete()
    #     reaction_context = dragon.gain_xp(task.xp_reward)

    #     user_state.record_task_complete()

    #     active_tasks.remove(task)
    #     completed_tasks.append(task)

    #     task.refresh_active_tasks()
    #     task.refresh_completed_tasks()

    #     status_label.config(text=dragon.get_status_text())
    #     if reaction_context:
    #         message = dragon.react(reaction_context, user_state)
    #     else:
    #         message = dragon.react("task_complete", user_state)
        
    #     return message_label.config(text=message)

class Dragon:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 100

        #Personality
        self.personality = "neutral"
        self.role_bias = "mentor"
        
        #Core Stats
        self.strength = 1
        self.dexterity = 1
        self.intelligence = 1
        self.charisma = 1
        self.growthpoints = 0
        self.stage = "Hatchling"

    def gain_xp(self, amount):
        self.xp += amount

        #Make the Dragon Level Up
        if self.xp >= self.xp_to_next_level:
            self.level_up()
            return "level_up"
        return None

    def level_up(self):
        self.level += 1
        
        self.xp = self.xp - self.xp_to_next_level
        self.xp_to_next_level = int(self.xp_to_next_level * 1.5)
        if self.xp >= self.xp_to_next_level:
            self.level_up()  # Handle multiple level-ups

        self.award_growth_points()
        self.update_stage()

    def award_growth_points(self):
        self.growthpoints += 1  # 1 growth point per level
        if self.level == 4:
            self.growthpoints += 2
        elif self.level == 7:
            self.growthpoints += 4

    # def increase_stat(stat_name):
    #     success = dragon.spend_growth_point(stat_name)
    #     if success:
    #         user_state.idle_cycles = 0
    #         user_state.last_action = "stat_up"

    #         status_label.config(text=dragon.get_status_text())
    #         message_label.config(text=dragon.react("stat_up", user_state))
    #     else:
    #         message_label.config(text=dragon.react("no_points", user_state))

    def update_stage(self):
        if self.level >= 7:
            self.stage = "Young Dragon"
        elif self.level >= 4:
            self.stage = "Wyrmling"
        else:
            self.stage = "Hatchling"

    def react(self, context):
        role = self.get_role()

        if UserState.idle_cycles >= 3:
            return self.get_callout_line(role, "idle")

        if UserState.tasks_skipped >= 2:
            return self.get_callout_line(role, "avoidance")
        
        return self.get_standard_line(role, context)

    def get_status_text(self):
        return (
            f"🐉 {self.name} the Dragon\n"
            f"Level: {self.level} ({self.stage})\n"
            f"XP: {self.xp} / {self.xp_to_next_level}\n"
            f"Growth Points: {self.growthpoints}\n"
            f"STR: {self.strength} | DEX: {self.dexterity}\n"
            f"INT: {self.intelligence} | CHA: {self.charisma}\n"
        )

    def update_personality(self):
        stats = {
            "Strength": self.strength,
            "Dexterity": self.dexterity,
            "Intelligence": self.intelligence,
            "Charisma": self.charisma
        }
        
        max_value = max(stats.values())
        top_stats = [stat for stat, value in stats.items() if value == max_value]

        if len(top_stats) == 1:
            self.personality = top_stats[0].lower()
    
    def get_personality(self):
        return self.personality

    def get_role(self):
        stats = {
            "strength": self.strength,
            "dexterity": self.dexterity,
            "intelligence": self.intelligence,
            "charisma": self.charisma
        }
        max_value = max(stats.values())
        top_stats = [stat for stat, value in stats.items() if value == max_value]
        
        if len(top_stats) > 1:
            return self.role_bias
        
        dominant_stat = top_stats[0]

        if dominant_stat == "strength":
            return "enforcer"
        elif dominant_stat == "dexterity":
            return "playful"
        elif dominant_stat == "intelligence":
            return "mentor"
        elif dominant_stat == "charisma":
            return "companion"
        else:
            return self.role_bias

    def spend_growth_point(self, stat):
        if self.growthpoints <= 0:
            return False

        if stat == "strength":
            self.strength += 1
        elif stat == "dexterity":
            self.dexterity += 1
        elif stat == "intelligence":
            self.intelligence += 1
        elif stat == "charisma":
            self.charisma += 1
        else:
            print("Invalid stat.")
            return

        self.growthpoints -= 1
        self.update_personality()
        return True

    def get_ambient_thought(self):
        thoughts = {
            "strength": [
                "We should train again soon. Discipline builds power.",
                "Idleness dulls the blade.",
                "Every moment is a chance to grow stronger."
            ],
            "dexterity": [
                "Hehe, ready to jump back in?",
                "We could totally knock out a quick task!",
                "Sitting still is boring~"
            ],
            "intelligence": [
                "There is much yet to learn.",
                "I’ve been thinking about efficient study methods.",
                "Knowledge grows when it is pursued."
            ],
            "charisma": [
                "Hey… want to do something together?",
                "I like it when we’re productive as a team.",
                "We make a good pair, you know."
            ],
            "neutral": [
                "I am here.",
                "Whenever you’re ready.",
                "We will grow, in time."
        ]
        }

        options = thoughts.get(self.personality, thoughts["neutral"])
        return random.choice(options)

    def get_callout_line(self, role, situation):
        callouts = {
            "mentor": {
                "idle": "You’re stalling. That won’t get you where you want to go.",
                "avoidance": "Avoiding your work doesn’t make it disappear. Face it."
            },
            "companion": {
                "idle": "Hey… you’ve been zoning out. Wanna talk about it?",
                "avoidance": "You keep skipping things. Are you okay?"
            },
            "enforcer": {
                "idle": "Enough waiting. Move.",
                "avoidance": "Discipline is slipping. Fix it."
            },
            "playful": {
                "idle": "Aww, don’t be bored! Let’s do something fun!",
                "avoidance": "Hehe, you keep dodging your tasks! That’s silly!"
            }
        }

        return callouts.get(role, {}).get(situation, "")

    def get_standard_line(self, role, context):
        responses = {
            "mentor": {
                "task_complete": "Good. Progress is earned.",
                "stat_up": "Growth acknowledged.",
                "no_points": "We need more experience."
            },
            "companion": {
                "task_complete": "We did it!! I’m proud of you!",
                "stat_up": "Ooo~ you’re getting stronger!"
            },
            "enforcer": {
                "task_complete": "Objective complete.",
                "stat_up": "Power increased."
            },
            "playful": {
                "task_complete": "Yay! That was fun!",
                "stat_up": "Woohoo! I feel awesome!"
            }
        }

        return responses.get(role, {}).get(context, "") or "..."

class UserState:
    def __init__(self):
        self.tasks_completed = 0
        self.tasks_skipped = 0
        self.consecutive_skips = 0
        self.last_action = None
        self.idle_cycles = 0

    def record_task_complete(self):
        self.tasks_completed += 1
        self.consecutive_skips = 0
        self.idle_cycles = 0
        self.last_action = "task_complete"

    def record_skip(self):
        self.tasks_skipped += 1
        self.consecutive_skips += 1
        self.last_action = "skip"

    def record_idle(self):
        self.idle_cycles += 1
        self.last_action = "idle"

    def get_emotional_state(self):
        if self.consecutive_skips >= 3:
            return "overwhelmed"
        elif self.idle_cycles >= 3:
            return "disengaged"
        elif self.tasks_completed >= 5:
            return "motivated"
        return "neutral"

    # --- Idle Thought Update ---
    # def idle_update():
    #     UserState.record_idle()
    #     message = Dragon.react("idle", UserState)
    #     if not message:
    #         message = Dragon.get_ambient_thought()
    #     message_label.config(text=message)
    #     window.after(random.randint(15000,20000), UserState.idle_update)

