import tkinter as tk
class Note:
    def __init__(self, message, start, freq, end=None, method="popup"):
        self.message = message
        self.start = start
        self.freq = freq
        self.end = end
        self.method = method
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