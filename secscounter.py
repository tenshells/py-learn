# import tkinter
# from tkinter import messagebox 

# top = tkinter.Tk()

# def helloCallBack():
#    messagebox.showinfo( "Title Bar", "Hello World",**options="bruh")

# B = tkinter.Button(top, text ="Hello", command = helloCallBack)

# B.pack()
# top.mainloop()




# import tkinter as tk
    

# def write_slogan():
#     print("Tkinter is easy to use!")

# root = tk.Tk()
# frame = tk.Frame(root)
# frame.pack()

# button = tk.Button(frame, 
#                    text="QUIT", 
#                    fg="red",
#                    command=quit)
# button.pack(side=tk.LEFT)
# slogan = tk.Button(frame,
#                    text="Hello",
#                    command=write_slogan)
# slogan.pack(side=tk.LEFT)

# root.mainloop()




import tkinter as tk

counter = 0 
def counter_label(label):
  counter = 0
  def count():
    global counter
    counter += 1
    if (counter == 1):
      label.config(text="It's been " + str(counter) + " blah SECOND  since I'm on :O")
    elif( counter %2 ==0):
      label.config(text="It's been " + str(counter) + " even seconds since I'm on :O")
    else:
      label.config(text="It's been " + str(counter) + " _ODD seconds since I'm on :O")
    label.after(1000, count)
  count()


root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="dark green")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()