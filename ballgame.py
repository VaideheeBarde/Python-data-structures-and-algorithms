# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 21:49:35 2017

@author: Vaidehee
"""

from tkinter import *
import random
import time

tk = Tk()

WIDTH = 800
HEIGHT = 600
canvas = Canvas(tk, height = HEIGHT, width = WIDTH)
tk.title = ("Drawing")
canvas.pack()

ball1 = canvas.create_oval(10, 10, 60, 60, fill = "orange")
ball2 = canvas.create_oval(450, 450, 520,520, fill = "red")

x1speed = 1
y1speed = 5
x2speed = 2
y2speed = 3

while True:
    canvas.move(ball1, x1speed, y1speed)
    canvas.move(ball2, x2speed, y2speed)
    pos_one = canvas.coords(ball1)
    pos_two = canvas.coords(ball2)
    if pos_one[3] >= HEIGHT or pos_one[1] <=0:
        y1speed = -y1speed
    if pos_one[0] <=0 or pos_one[2] >= WIDTH:
        x1speed = -x1speed
    if pos_two[3] >= HEIGHT or pos_two[1] <= 0:
        y2speed = -y2speed
    if pos_two[0] <= 0 or pos_two[2] >= WIDTH:
        x2speed = -x2speed
        
    tk.update()
    time.sleep(0.01)
    
tk.mainloop()
