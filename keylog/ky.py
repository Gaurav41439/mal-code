from pynput import keyboard

print("🔐 Dummy Keylogger Started. Press ESC to stop.")

def on_press(key):
    try:
        print(f"[KEY] {key.char}")
    except AttributeError:
        print(f"[SPECIAL] {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        print("🛑 Exiting keylogger.")
        return False  # Stops listener

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
