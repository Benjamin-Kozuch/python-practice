from Tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master) # Wrapping the Root in a Frame
        frame.pack() #After creating the widget, we immediately call the pack method to make the frame visible.

        #The button instances are stored in instance attributes.
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit) #fg = foreground
        self.button.pack(side=LEFT)
        
        #The button instances are stored in instance attributes.
        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "hi there, everyone!"

root = Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below