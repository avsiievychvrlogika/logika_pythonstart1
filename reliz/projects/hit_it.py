from turtle import *
import time
from random import *
s_width = 200
s_height = 180



class Sprite(Turtle):
    def __init__(self, x, y, step=10, shape='circle', color='black'):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color(color)
        self.shape(shape)
        self.step = step



    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)

    def is_collide(self, sprite):
        return self.distance(sprite.xcor(), sprite.ycor()) < 30

    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.setheading(self.towards(x_end, y_end))

    def make_step(self):
        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start)

player = Sprite(0, -100, 10, 'circle', 'orange')
goal = Sprite(0, 120, 20, 'triangle', 'green')
level = input("Виберіть рівень: easy, medium, hard: ").lower()

scr = player.getscreen()

if level == 'easy':
    scr.bgcolor('skyblue')
    enemy_speed = 10    
    enemy_positions = [(-s_width, 0), (s_width, 70)]
elif level == 'medium':
    scr.bgcolor('mediumpurple')
    enemy_speed = 20    
    enemy_positions = [(-s_width, 0), (s_width, 70), (-s_width, 40), (s_width, 100),
                       (20, 0), (20,-20), (-20, 0), (-20,-20)]
elif level == 'hard':
    scr.bgcolor('blue')
    enemy_speed = 40
    enemy_positions = [(-s_width, 0), (s_width, 70), (-s_width, 40), (s_width, 100),
                       (20, 0), (20,-20), (-20, 0), (-20,-20)]
else:
    scr.bgcolor('grey')
    enemy_speed = 6
    enemy_positions = [(-s_width, 0), (s_width, 70)]
enemies = []
i=0
for pos in enemy_positions:
    i=randint(1, 3)
    if i % 3 == 0:
        direction = (pos[0], -pos[1])
    elif i % 3 == 1:   
        direction = (-pos[0], -pos[1])
    elif i % 3 == 2:
        direction = (-pos[0], pos[1])

    enemy = Sprite(pos[0], pos[1], enemy_speed, 'square', 'red')
    enemy.set_move(pos[0], pos[1], direction[0], direction[1])
    enemies.append(enemy)
    i+=1

scr.listen()

scr.onkey(player.move_down, 'Down')
scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_right, 'Right')
scr.onkey(player.move_left, 'Left')

total_score = 0
game_over = False
start_time = time.time()  



while not game_over and total_score < 3:
    scr.update()
    
    elapsed_time = time.time() - start_time  

    if elapsed_time > 15:  
        player.goto(0, 0)
        player.write("YOU LOSE!", align="center", font=("Arial", 24, "bold"))
        game_over = True
        break

    
    for enemy in enemies:
        if level == 'hard': 
            if randint(1,2)==2:
                enemy.make_step()
        else:
            enemy.make_step()
    
    if player.is_collide(goal):
        player.goto(0, -100)
        total_score += 1

    
    for enemy in enemies:
        if player.is_collide(enemy):
            player.goto(0, 0)
            player.write("YOU LOSE!", align="center", font=("Arial", 24, "bold"))
            goal.hideturtle()
            game_over = True
            break


if total_score >= 3:
    player.goto(0, 0)
    player.write("YOU WIN!", align="center", font=("Arial", 24, "bold"))


for enemy in enemies:
    enemy.hideturtle()

scr.mainloop()
