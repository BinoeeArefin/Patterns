from tkinter import N
import turtle
import colorsys

k1=turtle.Turtle()
turtle.Screen().bgcolor("black")
k1.pensize(2)
k1.speed(0)
n=36
h=0
for i in range(60):
    c=colorsys.hsv_to_rgb(h,1,0.9)
    h+=1/n
    k1.pencolor(c)
    k1.forward(i*4)
    k1.left(100)
    k1.forward(200)
    k1.left(200)
turtle.done()