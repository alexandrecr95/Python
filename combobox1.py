#importing tkinter class library
import tkinter as tk
from tkinter import ttk


#creating function for event
def on_select(event):
    
    #creating item object that handles value of selected_item
    selected_item = event.widget.get()
    print("Selected Item:", selected_item)
    
#creating root window
root = tk.Tk()
root.title("Combobox Example")

#creating static array
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

#creating widget object
combo_box = ttk.Combobox(root, values=items)
#obtaining event from combo box object
combo_box.bind("<<ComboboxSelected>>", on_select)

combo_box.pack()
#run mainloop to keep window open
root.mainloop()