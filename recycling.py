# # --- Task Lists ---
# active_tasks = [
#     Task("Math Homework", 100),
#     Task("English Essay", 200),
#     Task("Study Biology", 400),
#     Task("Clean Room", 50),
#     Task("Grocery Shopping", 75),
#     Task("Exercise for 30 minutes", 150),
#     Task("Read a Chapter of a Book", 120),
#     Task("Practice a Hobby", 180),
#     Task("Meditate for 10 minutes", 80),
#     Task("Plan the Week Ahead", 130),
#     Task("Organize Desk", 90),
#     Task("Call a Friend or Family Member", 110)
# ]
# completed_tasks = []

# # --- User State ---
# user_state = UserState()

# # --- Create Dragon ---
# dragon = Dragon("Ember")

# # --- Create Window ---
# window = tk.Tk()
# window.title("QuestPet")
# active_label = tk.Label(window, text="Active Quests")
# active_label.pack()

# active_listbox = tk.Listbox(window, width=40, height=6)
# active_listbox.pack(pady=5)

# completed_label = tk.Label(window, text="Completed Quests")
# completed_label.pack()

# completed_listbox = tk.Listbox(window, width=40, height=6)
# completed_listbox.pack(pady=5)



# # --- Label to Show Dragon Info ---
# status_label = tk.Label(window, text=dragon.get_status_text(), font=("Arial", 12))
# status_label.pack(pady=10)

# message_label = tk.Label(window, text="", font=("Arial", 10), fg="red")
# message_label.pack(pady=5)



# # --- Complete Task Button ---
# xp_button = tk.Button(window, text="Complete Task", command= Task.complete_task)
# xp_button.pack(pady=10)

# stat_frame = tk.Frame(window)
# stat_frame.pack(pady=10)

# # --- Stat Buttons ---
# tk.Button(stat_frame, text="Increase STR", command=lambda: Dragon.increase_stat("strength")).grid(row=0, column=0, padx=5)
# tk.Button(stat_frame, text="Increase DEX", command=lambda: Dragon.increase_stat("dexterity")).grid(row=0, column=1, padx=5)
# tk.Button(stat_frame, text="Increase INT", command=lambda: Dragon.increase_stat("intelligence")).grid(row=0, column=2, padx=5)
# tk.Button(stat_frame, text="Increase CHA", command=lambda: Dragon.increase_stat("charisma")).grid(row=0, column=3, padx=5)



# UserState.idle_update()

# # --- Start App ---
# window.mainloop()