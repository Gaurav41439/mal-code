import subprocess
import time

def open_terminal():
    subprocess.Popen(['open', '-a', 'Terminal'])

def show_alert():
    message = "System Warning!\nPossible infection detected."
    script = f'display dialog "{message}" with title "⚠️ Alert" buttons ["OK"] with icon caution'
    subprocess.call(['osascript', '-e', script])

try:
    while True:
        open_terminal()
        show_alert()
        time.sleep(2)
except KeyboardInterrupt:
    print("Timebomb manually stopped. You're safe now.")
