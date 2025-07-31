from turtle import *
from random import randint
ht()

def create_t(x, y, sh, col):
    t = Turtle()
    t.shape(sh)
    t.speed(0)
    t.color(col)
    t.pu()
    t.goto(x,y)
    return t


def draw_field():
    t = create_t(-150, -100, "turtle", "gold")
    t.ht()
    t.width(10)
    t.pd()
    
    #rectangle 300 x 200
    
def create_turtle(x, y, col):
    t = create_t(x, y, "circle", col)
   
    #drag    
    
    return t
   
tt = []

#colors
colors = []
for col in colors:
    #create and append

def create_label(x, y):
    t = create_t(x, y, "turtle", "violet")
    t.ht()
    def write_t(count):
        t.clear()
        t.write(f"In rect {count} turtle", font = ("Arial", 16))
       
    t.write_t = write_t
    return t
   
label = create_label(-150, -125)


def check_turtle():
    count = 0
    for t in tt:
        #check if in rect        
           
    label.write_t(count)

draw_field()    
check_turtle()
done()