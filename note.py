import sys
import time
import tkinter as tk
import json
import random

class Note:
    def __init__(self, message, end, freq=None):
        self.msg = message
        if freq:
            self.freq = freq
        else:
            self.freq = end//6
        if end == 0:
            self.end = time.time()*2
        else:
            self.end = end + time.time()
        self.last_snoozed = None
        self.total_snoozes = 0
        self.est_snoozes = end // self.freq

def popup():
    root = tk.Tk()
    root.title("HydraNote")
    root.geometry("200x80+300+100")  # width x height + x + y
    root.iconphoto(False, tk.PhotoImage(file="icon.png"))
    label = tk.Label(root, text=note.msg)
    label.pack(pady=10)

    button = tk.Button(root, text="Snooze", command=root.destroy)
    button.pack()

    root.mainloop()

# create Note information
note_data = json.loads(sys.argv[1])
note = Note(note_data["message"], end=note_data["time"])

# Wait and popup
while True:
    note.last_snoozed = time.time()
    time.sleep(note.freq)
    popup()
    note.total_snoozes += 1
    if note.end and time.time() > note.end:
        break

"""
This file should handle each individual note's processing.
"""