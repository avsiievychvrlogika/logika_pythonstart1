# Частина 1
#1
from art import *
x_start,y_start = -150,50
size = 100

def draw_field(x0,y0,a,c):
  width(4)
  x,y=x0,y0
  for i in range(3):
      for j in range(3):
          start(x,y)
          square(a,c)
          x+=a
      x=x0
      y-=a


#2

from art import *
def draw_cross(x,y,col):
  #твій код
    size = 100
    start(x,y)
    color(col)
    width(10)
    goto(x+size,y+size)
    start(x+size, y)
    goto(x,y+size)

#3

from art import *
def draw_zero(x,y,size,col):
    start(x + size//2,y)
    width(5)
    setheading(0)
    color(col)
    circle(size//2)

#4
#ігрове поле
playing_field = [None, -1,-1,-1,-1,-1,-1,-1,-1,-1]
#координати клітинок ігрового поля
x_cor = [None, -150,-50,50,-150,-50,50,-150,-50,50]
y_cor = [None, 50,50,50,-50,-50,-50,-150,-150,-150]
#розмір клітинок ігрового поля
size = 100

def move_player(player,col):
    cell = int(input("Введіть номер клітинки від 1 до 9"))
    while playing_field[cell]!=-1:
        print("Клітинки вже зайнята!")
        cell = int(input("Введіть номер клітинки від 1 до 9"))
    x = x_cor[cell]
    y = y_cor[cell]
    start(x,y)
    playing_field[cell] = player
    if player == 1:
        color(col)
        draw_cross(x,y,col)
    else:
        color(col)
        draw_zero(x,y,100,col)


#Частина 2
#1
def check_win():
    # 1 = 2 = 3
    if playing_field[1] == playing_field[2] == playing_field[3] :
        return playing_field[1]
    # 4 = 5 = 6
    if playing_field[4] == playing_field[5] == playing_field[6] :
        return playing_field[4]
    # 7 = 8 = 9
    if playing_field[7] == playing_field[8] == playing_field[9] :
        return playing_field[7]
    # 1 = 4 = 7
    if playing_field[1] == playing_field[4] == playing_field[7] :
        return playing_field[1]
    # 2 = 5 = 8
    if playing_field[2] == playing_field[5] == playing_field[8] :
        return playing_field[2]
    # 3 = 6 = 9
    if playing_field[3] == playing_field[6] == playing_field[9] :
        return playing_field[3]
    # 1 = 5 = 9
    if playing_field[1] == playing_field[5] == playing_field[9] :
        return playing_field[1]
    # 3 = 5 = 7
    if playing_field[3] == playing_field[5] == playing_field[7] :
        return playing_field[3]

    return -1  




#2

from art import*
from cross_dot import *
from random import randint
speed(0)
draw_field(-150,50,100,"green")

playing_field = [None, -1,-1,-1,-1,-1,-1,-1,-1,-1]
x_cor = [None, -150,-50,50,-150,-50,50,-150,-50,50]
y_cor = [None, 50,50,50,-50,-50,-50,-150,-150,-150]
size = 100


player = randint(0,1)
while True:
   
    if player == 1:
        move_player(player, "red")
        player = 0
    else:
        move_player(player, "yellow")
        player = 1
   
    win = check_win()
    if win == 1:
        print("Cross win")
        break
    elif win == 0:
        print("Dot win")
        break


from turtle import *
from art import*
from cross_dot import *
from random import randint
speed(0)
field("green")






playing_field = [None, -1,-1,-1,-1,-1,-1,-1,-1,-1]
x_cor = [None, -150,-50,50,-150,-50,50,-150,-50,50]
y_cor = [None, 50,50,50,-50,-50,-50,-150,-150,-150]
size = 100


player = randint(0,1)
while True:
   
    if player == 1:
        move_player(player, "red")
        player = 0
    else:
        move_player(player, "yellow")
        player = 1
   
    win,cell,h = check_win()
    if win == 1:
        crossOut(cell,h,"хрестик")
        break
    elif win == 0:
        crossOut(cell,h,"нулик")
        break
    if check_no_one_won():
        crossOut(cell,h,"нічія")
        break
 
