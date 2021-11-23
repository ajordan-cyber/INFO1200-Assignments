# This is the circumference calculator


# import the required modules (tkinter, locale, anything else we need)
import tkinter as tk
from tkinter import ttk, messagebox 



# populate the GUI
# add a button to calculate
# create an entry for the radius
# create a label for the radius
# create another label to show the circumference
# create another lavel for the circumference title

class CircumferenceFrame(ttk.Frame):
    # creates the main window, also loads data if needed, and UI controls
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent      

        # Define string variables for text entry fields
        self.radius = tk.StringVar()
        self.circumference = tk.StringVar()

        self.initComponents()

    def initComponents(self):
        self.pack()

        # Display the grid of labels and text entry fields
        ttk.Label(self, text="Radius:").grid(
            column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.radius).grid(
            column=1, row=0)

        ttk.Label(self, text="Circumference:").grid(
            column=0, row=3, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.circumference,
                  state="readonly").grid(
            column=1, row=3)

        # self.makeButtons()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)


# create function to define logic for the circumference



# add IF statement to check if the current module is the main module
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Circumference Calculator")
    CircumferenceFrame(root)
    root.mainloop()