import tkinter as tk
import json

root = tk.Tk()
root.title("Create Note")
root.geometry("300x150+300+100")  # width x height + x + y
root.iconphoto(True, tk.PhotoImage(file="icon.png"))


"""Gather message and time information from user"""
end_label = tk.Label(root, text="Time Until End")
end_label.grid(row=0, column=0)

mins_label = tk.Label(root, text="m")
mins_label.grid(row=1, column=0)

mins_inp = tk.Spinbox(root, from_=0, to=59, width=2)
mins_inp.grid(row=2, column=0)

hrs_label = tk.Label(root, text="h")
hrs_label.grid(row=1, column=1, pady=5)

hrs_inp = tk.Spinbox(root, from_=0, to=23, width=2)
hrs_inp.grid(row=2, column=1, pady=5)

days_label = tk.Label(root, text="d")
days_label.grid(row=1, column=2, pady=5)

days_inp = tk.Spinbox(root, from_=0, to=60, width=2)
days_inp.grid(row=2, column=2, pady=5)

message = tk.Entry(root, width=50, )
message.grid(row=3, column=0, columnspan=3, pady=5)


def create_note():
    # Placeholder for note creation logic
    # TODO: ERROR HANDLING FOR NOTE TIME INPUT
    note_time = int(mins_inp.get())*60 + int(hrs_inp.get())*3600 + int(days_inp.get())*86400
    note_data = {
        "message": message.get(),
        "time": note_time
    }
    print(json.dumps(note_data))
    root.destroy()

def confirm_creation():
    confirmation = tk.Toplevel(root)

    confirmation_label = tk.Label(confirmation, text="Are you sure?\nThis will create a new note.")
    confirmation_label.pack(pady=10)

    conf_yes = tk.Button(confirmation, text="Yes", command=create_note)
    conf_yes.pack(side="right", padx=10, pady=10)

    conf_no = tk.Button(confirmation, text="No", command=confirmation.destroy)
    conf_no.pack(side="left", padx=10, pady=10)

button = tk.Button(root, text="Add Note", command=confirm_creation)
button.grid(row=4, column=0, columnspan=3, pady=5)

root.mainloop()