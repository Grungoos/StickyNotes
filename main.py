import tkinter as tk

title = 'Sticky Notes'
geometry = '500x200'
width = 250
height = 150
topmost = '-topmost'
transparent = '-alpha'
window = tk.Tk()

todos = []


def update_transparency(value):
    window.attributes('-alpha', float(value))


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

def add_todo():
    todo_frame = tk.Frame(window)
    todo_frame.pack(fill='x')
    var = tk.IntVar()
    checkbox = tk.Checkbutton(todo_frame, variable=var)
    checkbox.pack(side='left')
    textfield = tk.Entry(todo_frame)
    textfield.pack(side='left', fill='x', expand=True)
    todos.append((checkbox, textfield))

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

# + Button
add_button = tk.Button(window, text="+", command=add_todo)
add_button.pack(side='bottom')

window.mainloop()