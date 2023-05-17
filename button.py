#import tkinter library
import tkinter as tk

#print function Button Clickled

def button_click():
    print("Button clicked!")
    
#create root window object
root = tk.Tk()
root.title("Button Example")

#create button widget
button = tk.Button(root,text="Click Me!", command=button_click)
button.pack()

#
root.mainloop()