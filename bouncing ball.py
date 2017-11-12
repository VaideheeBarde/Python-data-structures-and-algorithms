# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 22:15:30 2017

@author: Vaidehee
"""

from tkinter import *
import random
import time

tk = Tk()

HEIGHT = 600
WIDTH = 800
canvas = Canvas(tk, height = HEIGHT, width = WIDTH)
tk.title("Bouncing ball")
canvas.pack()

class Ball:
    def __init__(self, color, size):
        self.shape = canvas.create_oval(10, 10, size, size, fill = color)
        self.xspeed = random.randrange(1, 8)
        self.yspeed = random.randrange(1, 8)
        
    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.xspeed = -self.xspeed
            
newball1 = Ball("red", 60)
newball2 = Ball("green", 100)
newball3 = Ball("orange", 80)

while True:
    newball1.move()
    newball2.move()
    newball3.move()
    tk.update()
    time.sleep(0.01)
            