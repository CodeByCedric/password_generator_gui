'''GUI password generator'''

import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password(length=50):
    '''Function to generate password of desired length'''
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    pyperclip.copy(password)
    return password

def on_generate_button_click():
    '''Action on click: quit, default length, given length, or error'''
    user_input = entry.get()
    if user_input.lower() in ["q", "quit"]:
        exit_pw_generator()
    elif user_input == "":
        password = generate_password()
        show_password(password)
    else:
        try:
            password = generate_password(int(user_input))
            show_password(password)
        except ValueError:
            password = generate_password()
            messagebox.showerror(
                title="Invalid Input",
                message="Invalid value, a password with 50 characters was generated.")
            show_password(password)

def show_password(password):
    '''show password'''
    result_label.config(text=f"Password generated and copied to clipboard:\n {password}")

def exit_pw_generator():
    '''exit gui'''
    root.quit()

# GUI Set-Up
root = tk.Tk()
root.title("Password Generator")

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 225
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10, expand=True, fill='both')

label = tk.Label(
    frame,
    text="Enter desired password length (leave blank for default length of 50):")
label.pack()

entry = tk.Entry(frame, width=5, justify='center')
entry.pack(pady=5)

generate_button = tk.Button(frame, text="Generate Password", command=on_generate_button_click)
generate_button.pack(pady=5)

result_label = tk.Label(frame, text="", wraplength=380, anchor='w', justify='center')
result_label.pack(pady=5)

exit_button = tk.Button(frame, text="Exit", command=exit_pw_generator)
exit_button.pack(pady=5)

root.mainloop()
