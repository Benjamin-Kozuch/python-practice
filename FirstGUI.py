from Tkinter import *

root = Tk() #Always start by creating a root...never more than one. 

w = Label(root, text="Hello, world!") #Label is a widget

w.pack() #Helps with sizing

root.mainloop()