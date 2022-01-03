import tkinter as tk

root = tk.Tk() 
root.geometry("320x180")
e = tk.Entry(root, width = 10)
e.pack()

def prophecy():
    l = tk.Label(root, text='YO ' + e.get())
    l.pack()

b = tk.Button(root, text = "Forsee below change and add 10: ", command=prophecy)
b.pack()

root.mainloop()