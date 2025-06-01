#не забудь підключити модуль черепашка
from turtle import *

def square(l,c):
    color(c)
    for i in range(4):
        fd(l)
        left(90)
        
def rectangle(l,h,c):
    color(c)
    for i in range(2):
        fd(l)
        left(90)
        fd(h)
        left(90)
        
def triangle(l,c,w):
    color(c)
    width(w)
    for i in range(3):
        fd(l)
        left(120)
        
def square_fill(a, col):
  color(col)
  begin_fill()
  for i in range(4):
    fd(a)
    lt(90)
  end_fill()
    
def rectangle_fill(a,b, col):
  color(col)
  begin_fill()
  for i in range(2):
    fd(a)
    lt(90)
    fd(b)
    lt(90)
  end_fill()
def triangle_fill(a, col):
  color(col)
  begin_fill()
  for i in range(3):
    fd(a)
    lt(120)
  end_fill()
def circle_fill(a,col):
  color(col)
  begin_fill()
  circle(a)
  end_fill()
  
def start(x, y):
  penup()
  goto(x, y)
  pendown()
  
def fon(col1,col2):
  start(-350,100)
  width(400)
  color(col1)
  fd(900)
  
  start(-350,-150)
  width(250)
  color(col2)
  fd(900) 