from turtle import *
import colorsys

bgcolor('black')
speed(0)
pensize(2)

hue = 0.0

for i in range(600):
    color =colorsys.hsv_to_rgb(hue,1,1)
    pencolor(color)
    hue += 0.005
    right(i/2)
    circle(i * 0.45, i/2)
    forward(i/2)
    left(77+i/2)
    right(33+i/2)
    forward(i/2)
    left(77+i/2)
    right(33+i/2)




done()
input()
