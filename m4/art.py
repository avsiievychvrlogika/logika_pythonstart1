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
def square_fill2(a, col,col2):
  pencolor(col)
  fillcolor(col2)
  begin_fill()
  for i in range(4):
    fd(a)
    lt(90)
  end_fill()
def triangle_fill2(a, col,col2):
  pencolor(col)
  fillcolor(col2)
  begin_fill()
  for i in range(3):
    fd(a)
    lt(120)
  end_fill()
def circle_fill2(a,col,col2):
  pencolor(col)
  fillcolor(col2)
  begin_fill()
  circle(a)
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
def rectangle_fill2(a,b, col,col2):
  pencolor(col)
  fillcolor(col2)
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

    
#cloud(0,0,30,"blue")
def home(x,y,a,c1,c2):
    start(x,y)
    square_fill(a,c1)
    start(x,y+a)
    triangle_fill(a,c2)
    start(x+a//4,y+a//4)
    square_fill(a/2,c2)
#home(0,0,100,"brown","green")    
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
#christmas_tree(0,0,20,40,"brown","lightgreen")

def cloud(x,y,a,col):
    start(x,y)
    width(1)
    color(col)
    begin_fill()
    for i in range(5):
        circle(a,230)
        rt(150)
    end_fill()
    
#cloud(0,0,30,"blue")
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

    
#speed(0)
#tree(-100,-100,80,"brown","green")

def draw(x,y,pixel,pic,colors):
    x0=x
    for l in pic:
        for c in l:
            start(x,y)
            if c!="-":
                color=colors[int(c)]
                square_fill(pixel,color)
            x+=pixel
        x=x0
        y-=pixel
def square(a,w, col):
  color(col)
  width(w)
  for i in range(4):
    fd(a)
    lt(90)
def rectangle(a,b,w, col):
  color(col)
  width(w)
  for i in range(2):
    fd(a)
    lt(90)
    fd(b)
    lt(90)

def parallelogram(a, b, col):
  color(col)
  for i in range(2):
    fd(a)
    lt(125)
    fd(b)
    lt(55)
    
#parallelogram(50,120,"red")
def parallelogram(a, b, w, angel, col):
  color(col)
  width(w)
  angel2 = 180 - angel
  for i in range(2):
    fd(a)
    lt(angel)
    fd(b)
    lt(angel2)
    
#parallelogram(50,70,10,35,"red")
def polygon(a, n, col):
  color(col)
  angel = 360 / n
  for i in range(n):
    fd(a)
    lt(angel)
#polygon(50,5,"red")
def polygon(a, n,w, col):
  color(col)
  width(w)
  angel = 360 / n
  for i in range(n):
    fd(a)
    lt(angel)
#polygon(50,5,"red")
def parallelogram_fill(a, b, col):
  color(col)
  begin_fill()
  for i in range(2):
    fd(a)
    lt(125)
    fd(b)
    lt(55)
  end_fill()
def polygon_fill(a, n, col):
  color(col)
  angel = 360 / n
  begin_fill()
  for i in range(n):
    fd(a)
    lt(angel)
  end_fill()
def start_line(penCol, fillCol, w):
  pencolor(penCol)
  fillcolor(fillCol)
  width(w)

#start_line("red","green",10) 
def star(a, col):
  color(col)
  begin_fill()
  for i in range(5):
    fd(a)
    lt(144)
  end_fill()
  
#star(50,"red")


def star(a, w,col1, col2):
  start_line(col1, col2, w)
  begin_fill()
  for i in range(5):
    fd(a)
    lt(144)
  end_fill()
  
#star(100,10,"yellow","red")
def sun(a, col ):
  color(col)
  begin_fill()
  for i in range(18):
    fd(a)
    lt(100)
  end_fill()
  
#sun(150, "yellow")

def sun(a, w, col1, col2):
  start_line(col1, col2, w)
  begin_fill()
  for i in range(18):
    fd(a)
    lt(100)
  end_fill()
  
#sun(150,10,"orange", "yellow")
def moon(a,col1, col2):
  circle_fill(a, col1)
  lt(180) 
  penup()
  fd(a)
  pendown()
  rt(180)
  circle_fill(a, col2)
  
#moon(100,"yellow", "white")


def gradient_fon(red, green, blue):
  width(20)
  x, y = -400, 200
  for i in range(25):
    color(f"rgb({red}, {green}, {blue})")
    start(x, y)
    fd(800)
    blue -= 5 
    y -= 18
#speed(0)
#gradient_fon(20,120,200)
def coube(a, w, col1, col2):
  start_line( w, col1, col2)
  square_fill(a)
  lt(90)
  fd(a)
  rt(90)
  parallelogram_fill(a,a,30)
  fd(a)
  rt(90)
  parallelogram_fill(a,a,120)
  
#speed(0)  
#coube(50,5,"grey"," darkgrey")

def constellation(a, col):
  star(a, col)
  penup()
  setheading(110)
  fd(a)
  pendown()
  
  star(a, col)
  penup()
  setheading(20)
  fd(a)
  pendown()
  star(a, col)
  
  penup()
  setheading(295)
  fd(a)
  pendown()
  star(a, col)
  
  penup()
  setheading(285)
  fd(a)
  pendown()
  star(a, col)
  
#speed(0)
#constellation(30, "yellow")
def car(x, y, a, col1, col2):
  # кузов машинки
  start(x, y)
  start_line(4,col1,col2)
  rectangle_fill2(a,a//3,col1,col2)
  #перше колесо
  start(x+a//4, y-a//6)
  start_line(4,col2,col1)
  circle_fill2(a//6,col1,col2)
  #друге колесо
  start(x+a- a//4, y-a//6)
  start_line(4,col2,col1)
  circle_fill2(a//6,col1,col2)
  #кабіна машинки
  start(x+a//3, y+a//3)
  start_line(4,col1,col2)
  square_fill2(a//3,col1,col2)
  
  
#speed(0)
#car(0,-100,100,"red","orange")
def lantern(a,c):
  setheading(90)
  fd(a)
  setheading(0)
  width(a//12)
  fd(a//3)
  bk(2*a//3)
  fd(a//6)
  square_fill2(a//3,c,c)
  setheading(90)
  fd(a//3)
  setheading(0)
  width(a//8)
  fd(2*a//3)
  bk(3*a//3)
def road(x, y, a, b, col1, col2, col3):
  start(x, y)
  start_line(b, col1, col1)
  fd(a)
  start(x, y)
  start_line(b//20,"white", "white")
  c = a//20
  for i in range(12):
    fd(c)
    penup()
    fd(c)
    pendown()
  start(x-c, y+b//2)
  start_line(b//30,col2, col2)
  for i in range(22):
    square_fill2(c,col2,col2)
    fd(c)
    
  
  start_line(b//25, col3, col1)
  x = x+ c//2
  for i in range(7):
    start(x, y+ b//2)
    lantern(2*c,col3)
    x += 4*c
    
    

#speed(0)  
#road(-400,-50, 800, 300,"grey", "black","gold")
