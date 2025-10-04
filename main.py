import tkinter as tk
import sys



root = tk.Tk()
root.title("HydraNote")
root.geometry("300x150+100+100")  # width x height + x + y

label = tk.Label(root, text="Remember to take a break!")
label.pack(pady=10)

button = tk.Button(root, text="Snooze", command=root.destroy)
button.pack()

root.mainloop()
