from turtle import *
shape ("turtle")
def draw_square(l, c):
    color(c)
    forward(l)

for i in range(5):
    draw_square(i * 5, 'red')

mainloop()
