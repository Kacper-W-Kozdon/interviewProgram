import time
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *


class Window(): 
    def __init__(self): 
        
        self._shape_exists = False
        self._progress_window_exists = False
        self.progress_root = None
        self.canvas = None
        self.line = None
        self.step = 10
        self.animate = False
        # Creating the tkinter Window
        self.main_window()
        

    def Close(self):
        self.root.destroy()

    def progress_window(self):

        def increment():
            progress_bar.step(20)

        def decrement():
            progress_bar.step(-20)

        def display():
            print(progress_bar["value"])
        try:
            if self.progress_root is None:
                print("Opening new window")
                self.progress_root = Tk()
            self.progress_root.geometry("400x100")
        except TclError:
            print("Opening new window")
            self.progress_root = Tk()
            
        frame = Frame(self.progress_root)
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

        self._progress_window_exists = True
        
        self.progress_root.mainloop()
        
    def set_shape(self):
        if self._shape_exists is True:
            return None
        move_it_button = Button(self.root, text="Move it", command=self.make_it_move)
        move_it_button.pack()

        stop_it_button = Button(self.root, text="Stop it", command=self.make_it_stop)
        stop_it_button.pack()

        self.canvas = Canvas(self.root, bg="black", height=200, width=200)
        
        self.line = self.canvas.create_line(0,0,0,200, fill='white')
        self.canvas.pack()
        
        self._shape_exists = True

        del_shape_button = Button(self.root, text="Remove shape", 
                                  command= lambda: (self.canvas.pack_forget(), del_shape_button.pack_forget(),
                                  move_it_button.pack_forget(), stop_it_button.pack_forget(), self.__setattr__("_shape_exists", False)))
        del_shape_button.pack()

    def update_line(self):
        if self.animate is True:
            self.step = 10 if (self.canvas.coords(self.line)[0] < 200 and self.step == 10) else -10
            self.step = -10 if (self.canvas.coords(self.line)[0] > 0 and self.step == -10) else 10

            self.canvas.move(self.line, self.step, 0)
        
            self.root.after(50, self.update_line)


    def make_it_move(self):
        self.animate = True
        self.root.after(50, self.update_line)

    def make_it_stop(self):
        self.animate = False


    def main_window(self):
        self.root = Tk()
        self.root.geometry("512x512")
        
        # Button for closing 
        exit_button = Button(self.root, text="Exit", command=self.Close)
        exit_button.pack(pady=20)

        progress_button = Button(self.root, text="Progress window", command=self.progress_window)
        progress_button.pack(pady=20)

        shape_button = Button(self.root, text="Make shape", command=self.set_shape)
        shape_button.pack(pady=20)

        

        self.root.mainloop()


# Running test window

test = Window()
