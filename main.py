import tkinter as tk


title = 'Sticky Notes'
geometry = '500x200'
topmost = '-topmost'
transparent = '-alpha'

window = tk.Tk()
window.title(title)
window.geometry(geometry)  # Sie können die Größe des Fensters ändern
window.attributes(topmost, 1)  # Fenster bleibt immer im Vordergrund
window.attributes(transparent, 0.8)  # Fenster ist teilweise transparent

window.mainloop()