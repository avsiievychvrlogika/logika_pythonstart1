Задачі з уроку

Частина 1
Задача 1
from art import *
def home(x,y,a,c1,c2):
    start(x,y)
    square_fill(a,c1)
    start(x,y+a)
    triangle_fill(a,c2)
    start(x+a//4,y+a//4)
    square_fill(a/2,c2)
home(0,0,100,"brown","green")    

Задача 2
from art import *
def christmas_tree(x,y,a,b,c1,c2):
    speed(0)
    start(x,y)
    rectangle_fill(a,b,c1)
    x = x - (2*b - a)//2
    y += b
    for i in range(3):
        start(x,y)
        triangle_fill(2*b,c2)
        y += b - b//4

christmas_tree(0,0,20,40,"brown","lightgreen")

Частина 2
Задача 1

from art import *

def cloud(x,y,a,col):
    start(x,y)
    width(1)
    color(col)
    begin_fill()
    for i in range(5):
        circle(a,230)
        rt(150)
    end_fill()
    
cloud(0,0,30,"blue")

Задача 2

#підключи свій модуль art
from art import *

def tree(x, y, a, col1, col2):
  start(x, y)
  width(a//6)
  color(col1)
  setheading(90)
  fd(a)
  setheading(0)
  width(a//14)
  color(col2)
  b = a // 8
  step = b//3
  for i in range(25):
    fd(b)
    lt(90)
    b += step

    
speed(0)
tree(-100,-100,80,"brown","green")