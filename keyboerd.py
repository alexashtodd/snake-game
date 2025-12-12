from pynput import keyboard

def on_press(key):
    try:
        print(f"Pressed: {key.char}")
    except AttributeError:
        print(f"Pressed special key: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        print("Esc pressed — exiting.")
        return False  # Stop listener

print("Listening for key presses. Press ESC to exit.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
