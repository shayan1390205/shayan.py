import tkinter as tk
from tkinter import ttk
from PIL import ImageGrab
import pyautogui
import threading
import time

running = False

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def start_tracking():
    global running
    running = True
    track_color()

def stop_tracking():
    global running
    running = False

def track_color():
    def loop():
        while running:
            x, y = pyautogui.position()
            image = ImageGrab.grab(bbox=(x, y, x + 1, y + 1))
            rgb = image.getpixel((0, 0))
            hex_color = rgb_to_hex(rgb)

            label_rgb.config(text=f"RGB: {rgb}")
            label_hex.config(text=f"HEX: {hex_color}")
            label_pos.config(text=f"X: {x}  Y: {y}")
            color_preview.config(bg=hex_color)

            time.sleep(0.1)

    threading.Thread(target=loop, daemon=True).start()

# GUI setup
root = tk.Tk()
root.title("Color Picker")
root.resizable(False, False)

# Color preview square
color_preview = tk.Label(root, text="", width=6, height=3, bg="black")
color_preview.grid(row=0, column=0, rowspan=2, padx=10, pady=5)

# Labels
label_rgb = ttk.Label(root, text="RGB: ")
label_hex = ttk.Label(root, text="HEX: ")
label_pos = ttk.Label(root, text="X:    Y: ")

label_rgb.grid(row=2, column=0, sticky="w", padx=10, pady=2)
label_hex.grid(row=3, column=0, sticky="w", padx=10, pady=2)
label_pos.grid(row=4, column=0, sticky="w", padx=10, pady=2)

# Buttons
stop_button = ttk.Button(root, text="Stop", command=stop_tracking)
start_button = ttk.Button(root, text="Start", command=start_tracking)

stop_button.grid(row=5, column=0, pady=(10, 2))
start_button.grid(row=6, column=0, pady=(2, 10))

root.mainloop()
