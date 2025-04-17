import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)


speed(0)
bgcolor("black")
color("red")
penup()


begin_fill()
for i in range(600):
    k = i * 0.01 
    x = hearta(k) * 20
    y = heartb(k) * 20
    goto(x, y)
    pendown()
end_fill()

# Finaliza el dibujo
hideturtle()
done()
