from turtle import *
 
# ваш код
class Sprite(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.color(color)
 
    def collide(self, sprite):
        x = self.xcor()
        y = self.ycor()
 
        sx = sprite.xcor()
        sy = sprite.ycor()
        if abs(x - sx) < 20 and abs(y - sy) < 20:
            return True
        return False
class Player (Sprite):
    def __init__(self):
        super().__init__(0, -100, "orange")
        self.shape("circle")
        screen = self.getscreen()
        screen.onkey(self._left, "Left")
        screen.onkey(self._right, "Right")
        screen.onkey(self._up, "Up")
        screen.onkey(self._down, "Down")
    def _left(self):
        self.setheading(180)
        self.forward(10)
 
    def _right(self):
 
        self.setheading(0)
        self.forward(10)
 
    def _up(self):
        self.setheading(90)
        self.forward(10)
 
    def _down(self):
        self.setheading(-90)
        self.forward(10)
 
class Target(Sprite):
    def __init__(self):
        self.ycoords = (150, -150, 150, -150)
        super().__init__(0, 0, "green")
        self.shape("triangle")
        self.touch_count = 0
        self.move_next_point()
    def move_next_point(self):
        if self.touch_count<len(self.ycoords):
            self.goto(0,self.ycoords[self.touch_count])
            self.touch_count+=1
    def is_victory(self):
        return self.touch_count>=len(self.ycoords)
 
class Enemy (Sprite):
    def __init__(self, y, xmin, xmax, is_left):
        super().__init__(0, 0, "red")
        self.shape("square")
        self.xmin = xmin
        self.xmax = xmax
 
        if is_left:
            self.seth(0)
            self.goto(xmin,y)
        else:
            self.seth(180)
            self.goto(xmax,y)
    def move(self):
        self.fd(5)
        if self.xcor()>self.xmax:
            self.seth(180)
        elif self.xcor()<self.xmin:
            self.seth(0)
    def is_gameover(self, player):
        return self.collide(player)
ht()
pu()
 
screen=getscreen()
player=Player()
target=Target()
enemy1=Enemy(0,-150,150,True)
enemy2=Enemy(75,-150,150,False)
 
enemies=[enemy1,enemy2]
is_game=True
screen.listen()
 
def on_timer_handler():
 
    global is_game
 
    if target.collide(player):
        target.move_next_point()
 
    for e in enemies:
        e.move()
        if e.is_gameover(player):
            write("Ви програли", font=("Arial",48))
            screen.bgcolor("#aa0000")
            is_game=False
        elif target.is_victory():
            write("Ви виграли", font=("Arial",48))
            screen.bgcolor("#00aa00")
            is_game=False
    if is_game:
 
        screen.ontimer(on_timer_handler, 100)
 
 
on_timer_handler()