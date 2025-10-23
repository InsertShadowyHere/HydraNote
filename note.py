import tkinter as tk
class Note:
    def __init__(self, message, end, freq=None):
        self.message = message
        self.freq = freq
        if end == 0:
            self.end = None
        else:
            self.end = end
        self.last_snoozed = None


root = tk.Tk()
root.title("HydraNote")
root.geometry("200x80+300+100")  # width x height + x + y
root.iconphoto(False, tk.PhotoImage(file="icon.png"))
label = tk.Label(root, text="Remember to take a break!")
label.pack(pady=10)

button = tk.Button(root, text="Snooze", command=root.destroy)
button.pack()

root.mainloop()
"""
This file should handle each individual note's processing.
"""