
from turtle import *
shape('turtle')
def draw_square(l, c):
    color(c)
    for i in range(4):
        forward(length)
        left(90)

speed(-1)

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()
