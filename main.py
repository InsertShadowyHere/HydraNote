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

class Note:
    def __init__(self, message, start, freq, end=None, method="popup"):
        self.message = message
        self.start = start
        self.freq = freq
        self.end = end
        self.method = method
        self.last_snoozed = None

class HydraController:
    """Manages creation and error handling of note instances."""
    def __init__(self):
        self.processes = []

    def create_note_process(self):
        p = subprocess.Popen([EXE_PATH, "creator.py"])
        self.processes.append(p)

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

icon = Icon("HydraNote", icon=Image.open("icon.png"), title="HydraNote",
    menu=Menu(MenuItem("New Note", lambda: HydraController().create_note_process()),
         MenuItem("Quit", lambda: controller.stop())))

def start_tray_icon(ctrl):
    # Run the icon in its own thread
    threading.Thread(target=icon.run, daemon=True).start()

if __name__ == "__main__":
    controller = HydraController()
    start_tray_icon(controller)
    while True:
        time.sleep(5)