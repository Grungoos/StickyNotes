import tkinter as tk
from tkinter import messagebox
import pickle

title = 'Sticky Notes'
geometry = '500x200'
width = 250
height = 150
topmost = '-topmost'
transparent = '-alpha'
window = tk.Tk()


def save_todos():
    todo_data = [{'text': textfield.get(), 'checked': var.get()} for checkbox, var, textfield in todos]
    with open('todos.pkl', 'wb') as f:
        pickle.dump(todo_data, f)


def load_todos():
    try:
        with open('todos.pkl', 'rb') as f:
            loaded_todos = pickle.load(f)
            for todo in loaded_todos:
                add_todo(todo['text'], todo['checked'])
    except FileNotFoundError:
        messagebox.showerror("Error", "No file to load")


todos = []


def update_transparency(value):
    window.attributes(transparent, float(value))


def create_transparency_slider(parent):
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
    global is_pinned
    is_pinned = not is_pinned
    window.overrideredirect(is_pinned)


def add_todo(todo_text="", checked=0):
    todo_frame = tk.Frame(window)
    todo_frame.pack(fill='x')
    var = tk.IntVar(value=checked)
    checkbox = tk.Checkbutton(todo_frame, variable=var)
    checkbox.pack(side='left')
    textfield = tk.Entry(todo_frame)
    textfield.pack(side='left', fill='x', expand=True)
    textfield.insert(0, todo_text)
    todos.append((checkbox, var, textfield))


# window
window.title(title)
window.geometry(geometry)
window.minsize(width, height)
window.attributes(topmost, 1)
window.attributes(transparent, 1)

# pin and slider frame
frame = tk.Frame(window)
frame.pack(fill='x')  # Füllt das Frame in x-Richtung aus

# inner frame for slider and pin button
inner_frame = tk.Frame(frame)
inner_frame.pack(fill='x')  # Füllt das inner_frame in x-Richtung aus

# Slider
transparency_slider = create_transparency_slider(inner_frame)

# Pin
is_pinned = False
pin_button = tk.Button(inner_frame, text="Pin", command=pin_unpin_window)
pin_button.grid(row=0, column=1, sticky='e')  # Platziert den Button in der ersten Zeile und zweiten Spalte des Grids

# Setzt das weight der zweiten Spalte auf 1, sodass sie allen zusätzlichen Platz aufnimmt
inner_frame.grid_columnconfigure(1, weight=1)

# Bottom frame for buttons
bottom_frame = tk.Frame(window)
bottom_frame.pack(side='bottom')

# + Button
add_button = tk.Button(bottom_frame, text="+", command=add_todo)
add_button.pack(side='left')

# Save Button
save_button = tk.Button(bottom_frame, text="Save", command=save_todos)
save_button.pack(side='left')

# Load Button
load_button = tk.Button(bottom_frame, text="Load", command=load_todos)
load_button.pack(side='left')

window.mainloop()
