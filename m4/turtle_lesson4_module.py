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




# функція перевірки виграшу
def check_win():
    # 1 = 2 = 3
    if playing_field[1] == playing_field[2] == playing_field[3] and playing_field[1]!=-1:
        return playing_field[1],1,0
    # 4 = 5 = 6
    if playing_field[4] == playing_field[5] == playing_field[6] and playing_field[4]!=-1 :
        return playing_field[4],4,0
    # 7 = 8 = 9
    if playing_field[7] == playing_field[8] == playing_field[9]  and playing_field[7]!=-1:
        return playing_field[7],7,0
    # 1 = 4 = 7
    if playing_field[1] == playing_field[4] == playing_field[7]  and playing_field[1]!=-1:
        return playing_field[1],1,270
    # 2 = 5 = 8
    if playing_field[2] == playing_field[5] == playing_field[8]  and playing_field[2]!=-1:
        return playing_field[2],2,270
    # 3 = 6 = 9
    if playing_field[3] == playing_field[6] == playing_field[9]  and playing_field[3]!=-1:
        return playing_field[3],3,270
    # 1 = 5 = 9
    if playing_field[1] == playing_field[5] == playing_field[9]  and playing_field[1]!=-1:
        return playing_field[1],1,315
    # 3 = 5 = 7
    if playing_field[3] == playing_field[5] == playing_field[7]  and playing_field[3]!=-1:
        return playing_field[3],3,225


    return -1,0,0  # Ніхто не виграв
def check_no_one_won():
    return not(-1 in playing_field)
    
def crossOut(cell,h,who):
    x = x_cor[cell]
    y = y_cor[cell]
    if h == 0:
        y += size//2
        s= size*3
    elif h == 270:
        x+= size//2
        y+=size
        s = size*3
    elif h==315:
        y += size
        s =size*1.4*3
    else:
        y += size
        x+=size
        s =size*1.4*3
    if who != "нічія":
        start(x,y)
        setheading(h)
        color("#87FF00")
        width(7)
        fd(s)
    start(0,0)
    write(f"Виграв - {who}", font=("Arial",20,"bold"))
