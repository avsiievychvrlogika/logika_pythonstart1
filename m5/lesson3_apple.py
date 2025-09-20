from turtle import *
from random import randint, choice
ht()
screen = getscreen()
# ваш код
def create_t(x, y, sh, col):
    t = Turtle()
    t.speed(0)
    t.pu()
    t.color(col)
    t.shape(sh)
    t.setheading(270)
    t.goto(x, y)
    return t

def create_lbl(x, y, col,txt):
    l = create_t(x, y,"turtle", col)
    l.ht()
    l.count = -1

    def update(txt):
        l.count += 1
        l.clear()
        l.write(f"{txt} : {l.count}", font = ("Arial", 16))
    l.update = update


    def write_end(txt):
        l.goto(0,0)
        l.write(txt, font = ("Arial", 40))
        return True
    l.write_end = write_end


    l.update(txt)
    return l



screen.bgcolor("black")
pole = create_t(-150, 150, "turtle", "white")
pole.ht()
pole.begin_fill()
for _ in range(4):
    pole.fd(300)
    pole.lt(90)
pole.end_fill()

appels=[]
colors=["red","gold","green"]


def spawn_a():
    a = create_t(randint(-130, 130), 150, "circle", choice(colors))
    appels.append(a)
    def del_a(a):
        a.ht()
        appels.remove(a)
    a.del_a = del_a
  
    def move():
        a.fd(5)
    a.move = move
   
    def check_miss():
        if a.ycor() <= - 150:
            a.ht()
            appels.remove(a)
            miss.update( "Miss")
    a.check_miss = check_miss
  
    def check_catch():
        x, y = plt.xcor(), plt.ycor()
        if a.distance(x,y) <= 10:
            a.ht()
            appels.remove(a)
            catch.update("Catch")
    a.check_catch = check_catch
    
miss = create_lbl(-150,160, "red", "Miss")
catch = create_lbl(70, 160, "green", "Catch")

plt=create_t(0,-130,"square","pink")

def moveL():
    if plt.xcor()>-140:
        plt.seth(180)
        plt.fd(10)
        
def moveR():
    if plt.xcor()<140:
        plt.seth(0)
        plt.fd(10)
        
screen.onkey(moveL, "Left")
screen.onkey(moveR, "Right")
screen.listen()

def check_end():
    if miss.count>=3:
        return miss.white_end("Ви програли")
    if catch.count>=10:
        return catch.white_end("Ви виграли")
    return False
def game():
    if randint(1,30)==1:
        spawn_a()
    for a in appels:
        a.move()
        a.check_miss()
        a.check_catch()
    if not check_end():
        screen.ontimer(game,50)
spawn_a()
game()

done()