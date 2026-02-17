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

