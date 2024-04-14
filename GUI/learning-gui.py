import time
import math
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
        self.angle = 0
        self.move = False
        self.spin = False
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

        spin_it_button = Button(self.root, text="Spin it", command=self.make_it_spin)
        spin_it_button.pack()

        stop_it_button = Button(self.root, text="Stop it", command=self.make_it_stop)
        stop_it_button.pack()

        self.canvas = Canvas(self.root, bg="black", height=200, width=200)
        
        self.line = self.canvas.create_line(100,50,100,150, fill='white')
        self.canvas.pack()
        
        self._shape_exists = True

        del_shape_button = Button(self.root, text="Remove shape", 
                                  command= lambda: (self.__setattr__("move", False),
                                  self.__setattr__("spin", False),
                                  self.canvas.destroy(),
                                  del_shape_button.pack_forget(),
                                  spin_it_button.pack_forget(),
                                  move_it_button.pack_forget(), stop_it_button.pack_forget(), self.__setattr__("_shape_exists", False)))
        del_shape_button.pack()

    def update_line(self):

        if self.move is True:
            x1, y1, x2, y2 = self.canvas.coords(self.line)
            midx = (x1 + x2)/2
            self.step = 10 if (midx < 200 and self.step == 10) else -10
            self.step = -10 if (midx > 0 and self.step == -10) else 10
            x1 += self.step
            x2 += self.step
            self.canvas.coords(self.line, x1, y1, x2, y2)
        
        if self.spin is True:
            self.angle += 1
            self.angle = self.angle if self.angle < 60 else 0
            x1, y1, x2, y2 = self.canvas.coords(self.line)
            midx = (x1 + x2)/2
            midy = (y1 + y2)/2
            x1 = midx + 50 * math.sin(self.angle * math.pi/60)
            x2 = midx - 50 * math.sin(self.angle * math.pi/60)
            y1 = midy - 50 * math.cos(self.angle * math.pi/60)
            y2 = midy + 50 * math.cos(self.angle * math.pi/60)
            self.canvas.coords(self.line, x1, y1, x2, y2)

        if any([self.spin, self.move]):
            self.root.after(50, self.update_line)

    def make_it_move(self):
        if self.move == True:
            return None
        self.move = True
        self.update_line()

    def make_it_spin(self):
        if self.spin == True:
            return None
        self.spin = True
        self.update_line()
        

    def make_it_stop(self):
        self.move = False
        self.spin = False


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
