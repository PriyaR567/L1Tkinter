import tkinter as tk
import random
window = tk.Tk()

window.geometry
color=["red","yellow","blue","green","pink"]
b = tk.Button(text="Click me",bg=random.choice(color))
b.pack()
window.mainloop()
