# функція малювання ігрового поля
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
# функція малювання хрестика
def draw_cross(x,y,col):
  #твій код
    size = 100
    start(x,y)
    color(col)
    width(10)
    goto(x+size,y+size)
    start(x+size, y)
    goto(x,y+size)
# функція малювання нулика
def draw_zero(x,y,size,col):
    start(x + size//2,y)
    width(5)
    setheading(0)
    color(col)
    circle(size//2)

# функція ходу гравця
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

# функція перевірки виграшу
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

    return -1  # Ніхто не виграв