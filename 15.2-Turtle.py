"""
Write a function called draw_rect that takes a Turtle 
object and a Rectangle and uses the Turtle to draw 
the Rectangle. See Chapter 4 for examples using 
Turtle objects.

Write a function called draw_circle that takes a 
Turtle and a Circle and draws the Circle.
"""

import turtle
import math

def draw_rect(length, width):
    """Draws a rectangle with sides of the given length and width.

    Returns the Turtle to the starting position and location.
    """
    for i in range(2):
        t.fd(width)
        t.lt(90)
        t.fd(length)
        t.lt(90)

def draw_circle(radius):

    arc_length = 2 * math.pi * radius
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(360) / n

    t.lt(step_angle/2)
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
    t.rt(step_angle/2)

t = turtle.Turtle()

length = int(input('rect_length: '))
width = int(input('rect_width: '))
draw_rect(length, width)

t.reset()

radius = int(input('circle radius: '))
draw_circle(radius)

t.mainloop()




    
    

