from turtle import*
import random
title('jugando')
bgcolor('black')
#pencolor('white')
"""
forward(100)
right(90)
forward(100)
left(90)
forward(100)
backward(50)
right(90)
forward(100)
"""
#circulo
"""
circle(60)
circle(100)
"""
"""
#cuadrado
pencolor('red')
pensize(3)
forward(100)
right(90)
penup()
pensize(5)
pencolor('green')
forward(100)
right(90)
pendown()
pensize(7)
pencolor('yellow')
forward(100)
right(90)
penup()
pensize(9)
pencolor('blue')
forward(100)
"""
"""
fillcolor('green')
begin_fill()
for i in range(4):
    
    forward(100)
    right(90)
end_fill()
"""
speed(0)
x=1
while x<400:
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colormode(255)
    pencolor(r,g,b)
    forward(5+x)
    right(200)
    x+=1


mainloop()