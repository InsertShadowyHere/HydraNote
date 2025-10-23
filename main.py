import json
import os
import tkinter as tk
import sys
import threading
import datetime
# from note import Note
import subprocess
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw
import threading
import time

EXE_PATH = sys.executable

class HydraController:
    """Manages creation and error handling of note instances."""
    def __init__(self):
        self.processes = []

    def create_note(self):
        result = subprocess.run([EXE_PATH, "creator.py"], capture_output=True, text=True)
        if result.returncode == 0 and result.stdout:
            proc = subprocess.Popen([EXE_PATH, "note.py", result.stdout])
            self.processes.append(proc)


    def stop(self):
        for note in self.processes:
            try:
                note.kill()
            except:
                pass
        os._exit(0)

def create_image():
    image = Image.new("RGB", (64, 64), "white")
    draw = ImageDraw.Draw(image)
    draw.ellipse((8, 8, 56, 56), fill="red")
    return image

# TODO: MAKE MENU ITEMS UPDATE WITH LISTS RUNNING
icon = Icon("HydraNote", icon=Image.open("icon.png"), title="HydraNote",
    menu=Menu(MenuItem("New Note", lambda: HydraController().create_note_process()),
         MenuItem("Quit", lambda: controller.stop())))

def start_tray_icon():
    # Run the icon in its own thread
    threading.Thread(target=icon.run, daemon=True).start()

if __name__ == "__main__":
    controller = HydraController()
    start_tray_icon()
    while True:
        time.sleep(5)