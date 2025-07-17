# ваш код
from turtle import *
from time import sleep
from random import randint

def create_turtle(x, y, w, h, col, sh):
    t=Turtle()
    t.color(col)
    t.shape(sh)
    t.speed(0)
    t.width(w)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.seth(h)
    return t
    
    
x_start, x_finish = -150, 150 

def draw_pole(col1, col2):
    pole=create_turtle(x_start, -150, 10, 90, col1, "triangle")
    pole.fd(300)
    pole.ht()
    
    pole2=create_turtle(x_finish, -150, 20, 90, col2, "triangle")
    pole2.fd(300)
    pole2.ht()
    
    pole3=create_turtle(-50, -50, 10, 90, "blue", "triangle")
    
    for i in range(3,0,-1):
        pole3.write(str(i),font=("Arial",50))
        sleep(1)
        pole3.clear()
    pole3.write("START",font=("Arial",50))
    sleep(1)
    pole3.ht()
    pole3.clear()
    
    
t1=create_turtle(x_start, -100, 5, 0, "pink", "turtle")
t2=create_turtle(x_start, 100, 5, 0, "gold", "turtle")

draw_pole("red","green")

while t1.xcor() < x_finish and t2.xcor() < x_finish:
    t1.fd(randint(1,5))
    t2.fd(randint(1,5))
    
if t1.xcor()>=x_finish:
    t1.penup()
    t1.goto(0,0)
    t1.pendown()
    t1.write("I am winner!", font=("Arial",20))
    for i in range(36):
        t1.lt(10)
        sleep(0.2)
elif t2.xcor()>=x_finish:
    t2.penup()
    t2.goto(0,0)
    t2.pendown()
    t2.write("I am winner!", font=("Arial",20))
    for i in range(36):
        t2.lt(10)
        sleep(0.2)
