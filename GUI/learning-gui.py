import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *


class Window(): 
    def __init__(self): 
        
        self._shape_exists = False
        self._progress_window_exists = False
        # Creating the tkinter Window
        
        

        self.root = Tk()
        self.root.geometry("512x256")



        # Button for closing 
        exit_button = Button(self.root, text="Exit", command=self.Close)
        exit_button.pack(pady=20)

        progress_button = Button(self.root, text="Progress window", command=Window.progress_window)
        progress_button.pack(pady=20)

        shape_button = Button(self.root, text="Make shape", command=self.set_shape)
        shape_button.pack(pady=20)

        self.root.mainloop()

    def Close(self):
        self.root.destroy()

    def progress_window():

        def increment():
            progress_bar.step(20)

        def decrement():
            progress_bar.step(-20)

        def display():
            print(progress_bar["value"])

        root = Tk()
        root.geometry("400x100")
        frame = Frame(root)
        progress_bar = Progressbar(frame, mode='determinate')
        progress_bar.pack(padx=10, pady=10)

        button = Button(frame, text="Increase", command=increment)
        button.pack(padx=10, pady=10, side=tk.LEFT)

        button = Button(frame, text="Decrease", command=decrement)
        button.pack(padx=10, pady=10, side=tk.LEFT)

        button = Button(frame, text="Display", command=display)
        button.pack(padx=10, pady=10, side=tk.LEFT)

        sizegrip = Sizegrip(frame)
        sizegrip.pack(expand=True, fill=tk.BOTH, anchor=tk.SE)

        frame.pack(padx=5, pady=5)
        root.mainloop()

    def set_shape(self):
        if self._shape_exists == True:
            return None

        canvas = Canvas(self.root, bg="blue", height=100, width=100)

        line = canvas.create_line(10,10,200,200, fill='white')
        canvas.pack()
        self._shape_exists = True

        del_shape_button = Button(self.root, text="Remove shape", command= lambda: (canvas.pack_forget(), del_shape_button.pack_forget(), self.__setattr__("_shape_exists", False)))
        del_shape_button.pack()



# Running test window

test = Window()
