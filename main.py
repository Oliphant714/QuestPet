import pygame
import sys
import tkinter as tk
# from Personality import Dragon
# from Personality import UserState
# from Personality import Task

root = tk.Tk()
root.title("QuestPet")

root.overrideredirect(True)
root.attributes("-topmost", True)

root.bind("<Escape>", lambda e: root.destroy())

root.config(bg="green")
root.wm_attributes("-transparentcolor", "green")

root.geometry("+0+500")

blob_img = tk.PhotoImage(file="visuals/assets/idle/i_1_blob.png")

blob_label = tk.Label(root, image=blob_img, bg="green")
blob_label.pack()

idle_frames = [
    tk.PhotoImage(file=f"visuals/assets/idle/i_{i}_blob.png") for i in range(1, 4)
]
frame_index = 0

def idle_animation():
    global frame_index

    blob_label.config(image=idle_frames[frame_index])
    frame_index = (frame_index + 1) % len(idle_frames)
    
    root.after(200, idle_animation)




idle_animation()
root.mainloop()