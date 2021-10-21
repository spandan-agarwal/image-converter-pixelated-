import time
import turtle
import pyautogui

time.sleep(2)
minimum = pyautogui.position()
print(minimum)
time.sleep(2)
max_x, max_y = pyautogui.position()
print(max_x, max_y)#I use the first point as the top left corner, and the second as the bottom right.

wn = turtle.Screen()
t = turtle.Turtle()
wn.colormode(255)#Allows RGB colors
t.pensize(2)
t.speed(0)
wn.setup(width = 1.0, height = 1.0)
wn.bgcolor("black")
x, y = minimum
min_x, min_y = minimum

def turtlemove(x, y):
    t.pu()
    t.goto(x - 965, 565 - y)#Compared coordinates in pyautogui with positions in turtle so they match.

def circle():
    t.pd()
    t.begin_fill()
    t.circle(2.9)
    t.end_fill()
    t.pu()

screenshot = pyautogui.screenshot()
while x != max_x and y != max_y:
    coordinate = x, y
    color = screenshot.getpixel(coordinate)
    t.pencolor(color)
    t.fillcolor(color)
    turtlemove(x, y)
    circle()
    if x < max_x:
        x += 6
    else:
        x = min_x
        y += 6
        #if y >= max_y:
            #break
print(t.pos())

wn.exitonclick()