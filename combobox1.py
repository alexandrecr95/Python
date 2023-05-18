#importing tkinter class library
import tkinter as tk
from tkinter import ttk


#creating function for event
def on_select(event):
    
    #creating item object that handles value of selected_item
    selected_item = event.widget.get()