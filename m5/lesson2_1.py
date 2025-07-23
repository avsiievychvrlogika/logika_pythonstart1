# ваш код
from turtle import *
from random import randint
from time import sleep

ht()
def create_t(x, y, h, col):
    t = Turtle()
    t.color(col)
    t.shape("turtle")
    t.setheading(h)
    t.pu()
    t.goto(x, y)
    t.pd()
    return t

screen = getscreen()
screen.bgcolor("yellow")

cl = create_t(200, 100, 0, "blue")
cl.count = 0
cl.ht()
cl.write(f"Клік: {cl.count}", font = ("Arial", 24))

run = create_t(200, 150, 0, "red")
run.count = 0
run.ht()
run.write(f"Втечі: {run.count}", font = ("Arial", 24))


t1 = create_t(0,0,0,"pink")
t2 = create_t(0,0,90,"violet")
t3 = create_t(0,0,180,"lightblue")
t4 = create_t(0,0,270,"gold")
def add_write_count():
    cl.count += 1
    cl.clear()
    cl.write(f"Click: {cl.count}", font = ("Arial", 24))

def click1(x, y):
    t1.lt(randint(30,200))
    add_write_count()
   
def click2(x, y):
    t2.lt(randint(30,200))
    add_write_count()
   
def click3(x, y):
    t3.lt(randint(30,200))
    add_write_count()
   
def click4(x, y):
    t4.lt(randint(30,200))
    add_write_count()
   
t1.onclick(click1)
t2.onclick(click2)
t3.onclick(click3)
t4.onclick(click4)

def check_run(t):
    if abs(t.xcor()) < 200 and abs(t.ycor()) < 200:
        t.fd(2)
    else:
        run.count += 1
        run.clear()
        run.write(f"Втечі: {run.count}", font = ("Arial", 24))

while cl.count < 20 and run.count < 4:
    check_run(t1)
    check_run(t2)
    check_run(t3)
    check_run(t4)
    sleep(0.1)
       
if cl.count >= 20:
    cl.pu()
    cl.goto(0,0)
    cl.write("You winn", font = ("Arial", 40))
if run.count >= 4:
    run.pu()
    run.goto(0,0)
    run.write("You lose", font = ("Arial", 40))