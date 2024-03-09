import tkinter as tk
from tkinter import messagebox
import json

title = 'Sticky Notes'
geometry = '500x200'
width = 250
height = 150
topmost = '-topmost'
transparent = '-alpha'
window = tk.Tk()

todos = []


def save_todos():
    # Collect todo data from the interface
    todo_data = [{'text': textfield.get(), 'checked': var.get()}
                 for checkbox, var, textfield, todo_frame, delete_button in todos]
    # Save todo data to a txt file in JSON format
    with open('todos.txt', 'w') as f:
        json.dump(todo_data, f)
    messagebox.showinfo("Save", "Todos have been saved.")


def load_todos():
    # Clear the current todo list
    for _, _, _, todo_frame, _ in todos:
        todo_frame.destroy()
    todos.clear()

    # Load todo data from the txt file
    try:
        with open('todos.txt', 'r') as f:
            loaded_todos = json.load(f)
            for todo in loaded_todos:
                add_todo(todo['text'], todo['checked'])
    except FileNotFoundError:
        messagebox.showerror("Error", "No file to load")
    except json.JSONDecodeError:
        messagebox.showerror("Error", "File is not in valid JSON format")


def update_transparency(value):
    # Update the transparency of the window
    window.attributes(transparent, float(value))


def create_transparency_slider(parent):
    # Create a slider for transparency setting
    slider = tk.Scale(parent,
                      from_=0.1, to=1, resolution=0.1,
                      command=update_transparency,
                      orient="horizontal", showvalue=0,
                      length=150,
                      sliderrelief='flat',
                      sliderlength=15,
                      troughcolor='blue',
                      )
    slider.set(1)
    slider.grid(row=0, column=0, sticky='w')
    return slider


def pin_unpin_window():
    # Toggle the window always on top state
    global is_pinned
    is_pinned = not is_pinned
    window.overrideredirect(is_pinned)


def remove_todo(index):
    # Remove a todo item and its widgets
    todos[index][3].destroy()
    del todos[index]
    # Update delete button commands because the indices have changed
    for i, (_, _, _, _, delete_button) in enumerate(todos):
        delete_button.config(command=lambda idx=i: remove_todo(idx))


def add_todo(todo_text="", checked=0):
    # Add a new todo item
    todo_frame = tk.Frame(window)
    todo_frame.pack(fill='x')
    var = tk.IntVar(value=checked)
    checkbox = tk.Checkbutton(todo_frame, variable=var)
    checkbox.pack(side='left')
    textfield = tk.Entry(todo_frame)
    textfield.pack(side='left', fill='x', expand=True)
    textfield.insert(0, todo_text)
    delete_button = tk.Button(todo_frame, text='X', command=lambda idx=len(todos): remove_todo(idx))
    delete_button.pack(side='right')
    todos.append((checkbox, var, textfield, todo_frame, delete_button))


def bind_keyboard_shortcuts():
    window.bind('<Control-n>', lambda event: add_todo())
    window.bind('<Control-s>', lambda event: save_todos())


# window configuration
window.title(title)
window.geometry(geometry)
window.minsize(width, height)
window.attributes(topmost, 1)
window.attributes(transparent, 1)

# frame for pin and transparency slider
frame = tk.Frame(window)
frame.pack(fill='x')

inner_frame = tk.Frame(frame)
inner_frame.pack(fill='x')

# transparency slider
transparency_slider = create_transparency_slider(inner_frame)

# pin button
is_pinned = False
pin_button = tk.Button(inner_frame, text="Pin", command=pin_unpin_window)
pin_button.grid(row=0, column=1, sticky='e')
inner_frame.grid_columnconfigure(1, weight=1)

# frame for control buttons
bottom_frame = tk.Frame(window)
bottom_frame.pack(side='bottom')

# add button
add_button = tk.Button(bottom_frame, text="+", command=lambda: add_todo())
add_button.pack(side='left')

# save button
save_button = tk.Button(bottom_frame, text="Save", command=save_todos)
save_button.pack(side='left')

# load button
load_button = tk.Button(bottom_frame, text="Load", command=load_todos)
load_button.pack(side='left')

# Bind keyboard shortcuts
bind_keyboard_shortcuts()

# Start the Tkinter event loop
window.mainloop()
